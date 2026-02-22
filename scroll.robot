*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***
${url}      https://www.amazon.in/

*** Test Cases ***
Verify scroll
        Open Browser        ${url}      chrome
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        Scroll Element Into View    xpath://div[normalize-space()='Make Money with Us']
        Sleep    2s
        Click Element    xpath://div[normalize-space()='Make Money with Us']
        Sleep    2s
        Title Should Be    Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in
        Close Browser


