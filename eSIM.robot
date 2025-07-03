*** Settings ***
Library    Orders.py


*** Variables ***
${package_name}   merhaba-7days-1gb


*** Test Cases ***
Authorization Request
    [Documentation]  Order 6 eSIMs with a specific package and validate the status of the orders.
    Log    "Getting OAuth2 token"
    ${auth_token}   Get OTHER Token
    Set Suite Variable    ${auth_token}  ${auth_token}
    Should Not Be Empty   ${auth_token}  "Authorization token should not be empty"


Order eSIMs
    [Documentation]  Place 6 eSIM orders and validate their status. Retuns a list of ICCIDs.
    Log   "Place 6 eSIM orders"
    ${iccids_list}  Place "6" eSIMs orders "${auth_token}" with "${package_name}"
    Set Suite Variable    ${iccids_list}  ${iccids_list}
    Should Not Be Empty   ${iccids_list}  "ICCID list should not be empty"


Validate Slug of eSIMs
    [Documentation]  Validate the ICCID and Package of the eSIMs in the response payload.
    Log  "Validating list of eSIMs...${iccids_list}"
    Get and Validate "6" eSIM order status "${auth_token}" and details "${iccids_list}"



*** Keywords ***
Get OTHER Token
    [Documentation]  Get OAuth2 token for API access
    ${token}  get_oauth_token
    RETURN   ${token}

Place "${count}" eSIMs orders "${token}" with "${package_name}"
    [Documentation]  POST an order for 6 merhaba-7days-1gb esims.
    ${response_payload}  place_esim_order   ${token}   ${count}   ${package_name}
    RETURN   ${response_payload}

Get and Validate "${count}" eSIM order status "${token}" and details "${response_payload}"
    [Documentation]  Get and validate the status of eSIM orders.
    ${esim_details}  sims_list   ${token}
    verify_esims  ${esim_details}   ${response_payload}  ${count}