*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***
${url}      https://jqueryui.com/datepicker/


*** Test Cases ***
Verify link text
        Open Browser        ${url}      chrome
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        Select Frame    xpath://iframe[@class='demo-frame']
        Sleep    2s
        Click Element    xpath://input[@id='datepicker']
        Sleep    2s
        Click Element    xpath://a[contains(text(),'21')]

        Close Browser


