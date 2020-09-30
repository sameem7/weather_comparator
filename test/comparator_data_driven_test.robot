*** Settings ***
Library         ${CURDIR}${/}../comparator.py
Test Template   Compare Temperature


*** Test Cases ***      {CITY_NAME}     {COUNTRY_CODE}
For Aligarh             Aligarh         IN
For Bellary             Bellary         IN
For Chennai             Chennai         IN
For Rajkot              Rajkot          IN    


*** Keywords ***
Compare Temperature 
    [Arguments]     ${CITY_NAME}    ${COUNTRY_CODE}

    Compare Temperature For     ${CITY_NAME}    ${COUNTRY_CODE}