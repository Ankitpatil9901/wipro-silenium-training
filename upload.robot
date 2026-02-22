*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***
${url}      https://the-internet.herokuapp.com/upload

*** Test Cases ***
Verify upload
        Open Browser        ${url}      firefox
        Maximize Browser Window
        Sleep    3s
        Wait Until Element Is Visible    xpath://input[@id='file-upload']
        Choose File    xpath://input[@id='file-upload']    "C:\Users\Hp\Downloads\virat.webp"
        Click Element    xpath://input[@id='file-submit']
        Wait Until Element Is Visible    xpath://h3[normalize-space()='File Uploaded!']

        Close Browser


#que -- https://www.tutorialspoint.com/selenium/practice/upload-download.php

