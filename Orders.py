import logging
import requests
import APILib
import Variables


import logging
import requests

def get_oauth_token():
    """
    Obtain an OAuth access token using client credentials.

    Returns:
        str: Access token string.

    Raises:
        requests.HTTPError: If the token request fails.
        KeyError: If the token is missing in the response.
    """
    url = f"{Variables.URL}{Variables.ENDPOINTS["TOKEN"]}"
    payload = {
        "grant_type": "client_credentials",
        "client_id": Variables.CILENT_ID,
        "client_secret": Variables.CLINET_PWD
    }

    logging.info("Requesting OAuth token from: %s", url)

    try:
        response = requests.post(
            url,
            data=payload,
            verify=False  # Consider removing or setting to True in production
        )
        response.raise_for_status()
        token_data = response.json()

        access_token = token_data["data"]["access_token"]
        logging.info("OAuth token acquired successfully.")

        return access_token

    except requests.exceptions.RequestException as e:
        logging.error("Failed to obtain OAuth token: %s", e)
        raise

    except KeyError:
        logging.error("Access token not found in response: %s", response.text)
        raise


def place_esim_order(token, quantity=6, package_id="merhaba-7days-1gb"):
    """
    Create an order for eSIMs via the Airalo API and return a list of ICCIDs.

    Args:
        quantity (int): Number of eSIMs to order.
        package_id (str): ID of the eSIM package.
        description (str): Description to identify the order.

    Returns:
        list: List of ICCIDs for the ordered eSIMs.

    Raises:
        RuntimeError: If the API response indicates failure.
    """
    url = f"{Variables.URL}{Variables.ENDPOINTS['ORDER']}"
    #token = APILib.get_oauth_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    form_data = {
        'quantity': (None, str(quantity)),
        'package_id': (None, package_id),
        'type': (None, 'sim'),
        'description': (None, "Order the eSIMs"),
        'brand_settings_name': (None, '')
    }

    logging.info("Sending order request to %s with payload: %s", url, form_data)

    try:
        response = requests.post(url, headers=headers, files=form_data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error("Failed to create order: %s", str(e))
        raise RuntimeError("Order creation failed due to request error") from e

    try:
        response_data = response.json()
    except ValueError:
        logging.error("Invalid JSON response received: %s", response.text)
        raise RuntimeError("Invalid JSON in response")

    logging.info("Order response received: %s", response_data)

    try:
        sims = response_data["data"]["sims"]
        iccids = [sim["iccid"] for sim in sims]
    except KeyError as e:
        logging.error("Missing expected data in response: %s", e)
        raise RuntimeError("Malformed response from API")

    return iccids



def sims_list(token):
    """
    Retrieve list of eSIMs from the API.

    Returns: List of eSIMs with their details.

    Raises:
        AssertionError: If expected ICCIDs are not found or response is invalid.
    """
    url = f"{Variables.URL}{Variables.ENDPOINTS['LIST_ESIM']}"
    #token = APILib.get_oauth_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    params = {
        "include": "order.status",
        "limit": 20
    }

    logging.info("Fetching eSIM list from: %s", url)
    response = requests.get(url, headers=headers, params=params)
    logging.info("API Response [%s]: %s", response.status_code, response.text)

    assert response.status_code == 200, f"Failed to fetch eSIM list: {response.status_code}"

    try:
        sims = response.json().get("data", [])
    except ValueError:
        raise AssertionError("Invalid JSON in eSIM list response")
    return sims



def verify_esims(act_reponse, expected_iccids=None, expected_count=6):
     """
    Validate a list of eSIMs from the API.

    Args:
        act_reponse (list): List of eSIMs from the API response.
        expected_iccids (list, optional): List of ICCIDs expected to be present.
        expected_count (int): Number of ICCIDs to validate (default is 6).

    Raises:
        AssertionError: If expected ICCIDs are not found or response is invalid.
    """
     match_count = 0
     if expected_iccids:
         for sim in act_reponse:
             iccid = sim.get("iccid")
             sim_status = sim.get("simable", {}).get("status", {}).get("slug")
             package_id = sim.get("simable", {}).get("package_id")

             logging.info("ICCID: %s | Status: %s | Package: %s", iccid, sim_status, package_id)

             if iccid in expected_iccids:
                 logging.info("Matched ICCID: %s (%d/%d)", iccid, match_count + 1, expected_count)
                 assert package_id == Variables.PAKAGE_NAME, \
                        f"Unexpected package ID for ICCID {iccid}: {package_id}"
                 match_count += 1

                 if match_count >= expected_count:
                     break
     assert match_count == expected_count, f"Only {match_count}/{expected_count} expected ICCIDs found."
     logging.info("✅ All expected ICCIDs verified successfully.")
