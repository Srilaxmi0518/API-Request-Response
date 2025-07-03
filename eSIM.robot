*** Settings ***
Library    Orders.py


*** Variables ***
${package_name}   merhaba-7days-1gb


*** Test Cases ***
Order_eSIM
    [Documentation]  Order 6 eSIMs with a specific package and validate the status of the orders.
    ${auth_token}   Get OTHER Token
    Log    "Getting OAuth2 token and Place 6 eSIM orders"
    ${iccids_list}  Place "6" eSIMs orders "${auth_token}" with "${package_name}"
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