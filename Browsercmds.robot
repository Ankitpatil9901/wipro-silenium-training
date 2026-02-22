*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***
${url}      https://the-internet.herokuapp.com/upload

*** Test Cases ***
Verify browsercmds
        Open Browser       ${url}      chrome
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        Go Back
        Sleep    2s
        Go To    ${url}
        Sleep    2s
        Close Browser


