*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***
${url}      https://the-internet.herokuapp.com/drag_and_drop

*** Test Cases ***
Verify drag drop
        Open Browser        ${url}      firefox
        Maximize Browser Window
        Sleep    3s
        Wait Until Element Is Visible    xpath://div[@id='column-a']
        Sleep    3s
        Drag And Drop    xpath://div[@id='column-a']    //div[@id='column-b']
        Sleep    3s



        
        Close Browser


#que -- https://www.tutorialspoint.com/selenium/practice/upload-download.php

