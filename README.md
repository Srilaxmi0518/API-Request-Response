# Airalo Partner API Automation

## Objective
Automate the creation and validation of eSIM orders using Airalo Partner API.

## Features
- OAuth2 Token generation
- Place order for 6 eSIMs (slug: merhaba-7days-1gb)
- Validate eSIM listing response

## How to Use
1. Install dependencies: `pip install requests`, 'pip install robotframework', 'pip install robotframework-requests'
2. Run: `robot .\eSIM.robot`
3. Verify console output for test success

## Author
Srilaxmi Buutkuri

## Test Case
API-Request-Response\eSIM.robot 

## Test Output
API-Request-Response\log\log.html

##  Console Output'
Started: API-Request-Response\eSIM.robot
==============================================================================
eSIM                                                                          
==============================================================================
[info] Requesting OAuth token from: https://sandbox-partners-api.airalo.com/v2/token
[info (+0.35s)] OAuth token acquired successfully.
[info] "Getting OAuth2 token and Place 6 eSIM orders"
[info] Sending order request to https://sandbox-partners-api.airalo.com/v2/orders  with payload: {'quantity': (None, '6'), 'package_id': (None, 'merhaba-7days-1gb'), 'type': (None, 'sim'), 'description': (None, 'Order the eSIMs'), 'brand_settings_name': (None, '')}
[info (+1.46s)] API Response [200] 
[info] ${iccids_list} = ['873000000000009177', '8936000000002513', '873000000000009178', '8936000000002514', '8936000000002515', '8936000000002516']
[info] "Validating list of eSIMs...['873000000000009177', '8936000000002513', '873000000000009178', '8936000000002514', '8936000000002515', '8936000000002516']"
[info] Fetching eSIM list from: https://sandbox-partners-api.airalo.com/v2/sims
[info (+0.63s)] API Response [200] 
Order_eSIM :: Order 6 eSIMs with a specific package and validate t... | PASS |
------------------------------------------------------------------------------
eSIM                                                                  | PASS |
1 test, 1 passed, 0 failed
==============================================================================
[info] ICCID: 8936000000002516 | Status: completed | Package: merhaba-7days-1gb
[info] Matched ICCID: 8936000000002516 (1/6)
Output:  C:\Users\Niranjan Reddy Dodda\PycharmProjects\API-Request-Response\log\output.xml
[info] ICCID: 8936000000002515 | Status: completed | Package: merhaba-7days-1gb
[info] Matched ICCID: 8936000000002515 (2/6)
[info] ICCID: 8936000000002514 | Status: completed | Package: merhaba-7days-1gb
[info] Matched ICCID: 8936000000002514 (3/6)
[info] ICCID: 873000000000009178 | Status: completed | Package: merhaba-7days-1gb
[info] Matched ICCID: 873000000000009178 (4/6)
[info] ICCID: 8936000000002513 | Status: completed | Package: merhaba-7days-1gb
[info] Matched ICCID: 8936000000002513 (5/6)
[info] ICCID: 873000000000009177 | Status: completed | Package: merhaba-7days-1gb
[info] Matched ICCID: 873000000000009177 (6/6)
[info] ✅ All expected ICCIDs verified successfully.
Log:     C:API-Request-Response\log\log.html
Report:  C:API-Request-Response\log\report.html

Robot Run Terminated (code: 0)