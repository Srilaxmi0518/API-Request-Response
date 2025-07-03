import logging

import requests
import Variables

proxies = {'http': 'http://[2a00:fbc:1150:1430:3eb9:3eb9:0:5002]:3128/'}



def get_oauth_token():
    url = Variables.token_url
    payload = {
        "grant_type": "client_credentials",
        "client_id": Variables.id,
        "client_secret": Variables.password
    }
    response = requests.post(url, data=payload, proxies={"http": None, "https": None}, verify=False)
    response.raise_for_status()
    logging.info(f'Request Payload: {payload} , \n Tokes are {response.json()}')
    return response.json()["data"]["access_token"]
