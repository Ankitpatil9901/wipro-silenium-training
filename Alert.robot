#Selecting by visible text
#Selecting by indexing
#Selecting the value

*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${url}      https://the-internet.herokuapp.com/javascript_alerts


*** Test Cases ***
Verify Alerts
        Open Browser        ${url}      chrome
        #maximise the browser window
        Maximize Browser Window
        Wait Until Element Is Visible    xpath= (//button)[1]
        Click Element    xpath:(//button)[1]
        # Informational alert - accept is for ok btn
        Handle Alert        action=ACCEPT       timeout=3
        Sleep    5s

        Click Element    xpath:(//button)[2]
        # Conformational alert - accept is for ok btn dismiss for cancel
        Handle Alert        action=DISMISS       timeout=3
        Sleep    5s
        #promt alert accept is for ok btn dismiss for cancel
        Click Element    xpath:(//button)[3]
        Input Text Into Alert    Hello
        Sleep    5s



        Close Browser




