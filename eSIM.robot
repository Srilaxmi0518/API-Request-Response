*** Settings ***
Library     Requests.py

*** Test Cases ***
Order_eSIM
    Log    "Getting OAuth2 token..."
    ${payload}  Get Credentials and place eSIM orders
    Log    ${payload}
    Log  "Validating list of eSIMs..."
    Get eSIM details
#     get_oauth_token()
#
#    print("Placing order for 6 eSIMs...")
#    order_response = create_order(token)

#    print("Validating list of eSIMs...")
#    list_esims(token)

*** Keywords ***
Get Credentials and place eSIM orders
    ${response_payload}  create_order
    RETURN   ${response_payload}

Get eSIM details
    list_esims
