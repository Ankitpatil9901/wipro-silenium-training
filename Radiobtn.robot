*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${url}      https://rahulshettyacademy.com/AutomationPractice/


*** Test Cases ***
Verify radio button
        Open Browser        ${url}      chrome
        #maximise the browser window
        Maximize Browser Window
        #wait untill the element
        Wait Until Element Is Visible    xpath://input[@value = 'radio1']
        #click on radio button
        Click Element    xpath://input[@value = 'radio1']
        Sleep    5
        #click on thecheck box 3
        Click Element    id=checkBoxOption3
        Sleep    5


        Close Browser
