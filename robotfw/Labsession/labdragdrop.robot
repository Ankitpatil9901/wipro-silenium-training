*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/droppable.php

*** Test Cases ***
Verify drag drop
        Open Browser        ${url}      firefox
        Maximize Browser Window
        Sleep    3s
        Wait Until Element Is Visible    xpath://div[@id='draggable']
        Sleep    3s
        Drag And Drop    xpath://div[@id='draggable']    //div[@id='draggable']
        Sleep    3s




        Close Browser


#que -- https://www.tutorialspoint.com/selenium/practice/upload-download.php

