*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/check-box.php


*** Test Cases ***
Verify Check Box
        Open Browser        ${url}      chrome
        #maximise the browser window
        Maximize Browser Window
        #wait untill the element
        Wait Until Element Is Visible    xpath://input[@id='c_bs_1']
        #click on main level1
        Click Element    xpath://input[@id='c_bs_1']
        Sleep    5
        #click on main level2
        Click Element    xpath://input[@id='c_bs_2']
        Sleep    5


        Close Browser
