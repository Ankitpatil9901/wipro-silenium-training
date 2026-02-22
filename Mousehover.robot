*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***
${url}      https://the-internet.herokuapp.com/hovers

*** Test Cases ***
Verify drag drop
        Open Browser        ${url}      firefox
        Maximize Browser Window
        Sleep    3s
        Wait Until Element Is Visible    xpath://div[@class='example']//div[1]//img[1]
        Mouse Over    xpath://div[@class='example']//div[1]//img[1]
        Sleep    2s
        Element Should Be Visible    xpath://h5[normalize-space()='name: user1']

        Close Browser


#que -- https://www.tutorialspoint.com/selenium/practice/upload-download.php

