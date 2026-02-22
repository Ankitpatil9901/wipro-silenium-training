*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***
${url}      https://the-internet.herokuapp.com/upload

*** Test Cases ***
Verify Screenshot
        Open Browser        ${url}      firefox
        Maximize Browser Window
        Sleep    3s
        Wait Until Element Is Visible    xpath://input[@id='file-submit']
        Capture Page Screenshot     "C:\Users\Hp\Downloads\AF_Mcqs.docx"
        Close Browser


#que -- https://www.tutorialspoint.com/selenium/practice/upload-download.php

