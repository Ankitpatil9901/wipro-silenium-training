*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***
${url}      https://www.amazon.in/

*** Test Cases ***
Verify drag drop
        Open Browser        ${url}      firefox
        Maximize Browser Window
        Set Selenium Implicit Wait    2s

        Sleep    3s
        Wait Until Element Is Visible    xpath://a[normalize-space()='Sell']
        Open Context Menu    xpath://a[normalize-space()='Sell']
        Sleep    3s
        #double click
        Double Click Element    xpath://a[normalize-space()='Mobiles']
        Sleep    3s
        Close Browser


