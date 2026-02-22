*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***
${url}      https://rahulshettyacademy.com/AutomationPractice/


*** Test Cases ***
Verify link text
        Open Browser       - ${url}      chrome
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        Click Element    xpath://button[@id='openwindow']
        @{windows}=     Get Window Names
        Log To Console    ${windows}
        @{titles}       Get Window Titles
        Log To Console    ${titles}
        Switch Window       title=QAClick Academy - A Testing Academy to Learn, Earn and Shine
        Element Text Should Be    xpath://a[@href='https://www.qaclickacademy.com']//img[@alt='Logo']
        Switch Window       MAIN

        Close Browser


