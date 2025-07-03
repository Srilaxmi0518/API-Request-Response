import logging

import requests

import APILib
import Variables


def create_order():
    url = Variables.token_url
    token = APILib.get_oauth_token()
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "esim_slug": "merhaba-7days-1gb",
        "quantity": 6
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 201, "Order creation failed"
    logging.info("Order Response:", response.json())
    return response.json()


def list_esims():
    url = Variables.esim_list
    token = APILib.get_oauth_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, "Failed to fetch eSIM list"
    esims = response.json()
    assert len(esims) == 6, f"Expected 6 eSIMs, found {len(esims)}"
    for esim in esims:
        assert esim["slug"] == "merhaba-7days-1gb", "Mismatched eSIM slug"
    logging.info("eSIMs verified successfully")

