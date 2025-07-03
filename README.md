# Airalo Partner API Automation

## Objective
Automate eSIM orders creation and validation test cases for Airalo Partner API Platform.

## Approach
Implement Robot Framework in Python with the following capabilities to automate API testing:
- Keyword-driven test suites
- Variable management for dynamic data
- HTTP request handling using Robot Framework Requests library
- Response validation and logging
- In-built execution report

## Features
- OAuth2 Token generation
- Place order for 6 eSIMs (slug: merhaba-7days-1gb)
- Validate eSIMs

## How to Use
1. Install dependencies: `pip install requests`, 'pip install robotframework', 'pip install robotframework-requests'
2. Run: `robot .\eSIM.robot`
3. Verify console output for test success

## Author
Srilaxmi Buutkuri

## Test Suite
Partner-API-Testing\eSIM.robot 

## Test Output
Partner-API-Testing\log\log.html

##  Console Output 
Partner-API-Testing> python -m robot .\eSIM.robot
==============================================================================
eSIM                                                                          
==============================================================================
Authorization Request :: Order 6 eSIMs with a specific package and... .
Authorization Request :: Order 6 eSIMs with a specific package and... | PASS |
------------------------------------------------------------------------------
Order eSIMs :: Place 6 eSIM orders and validate their status. Retu... | PASS |
------------------------------------------------------------------------------
Validate Slug of eSIMs :: Validate the ICCID and Package of the eS... | PASS |
------------------------------------------------------------------------------
eSIM                                                                  | PASS |
3 tests, 3 passed, 0 failed
==============================================================================
Output:  Partner-API-Testing\output.xml
Log:     Partner-API-Testing\log.html
Report:  Partner-API-Testing\report.html
