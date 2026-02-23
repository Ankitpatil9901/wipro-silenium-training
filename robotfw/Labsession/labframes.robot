*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/frames.php


*** Test Cases ***
Verify Frames
        Open Browser        ${url}      chrome
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        Select Frame    xpath://body//main//iframe[1]
        ${text}=    Get Text    xpath://header[@class='header selenium bg-white p-3 ']
        Log To Console    ${text}
        Unselect Frame
        Sleep    2s
        Select Frame    xpath://body//main//iframe[2]
        ${text}=    Get Text    xpath://header[contains(@class,'header selenium bg-white p-3')]
        Log To Console    ${text}
        Unselect Frame
        Sleep    2s


        Close Browser


