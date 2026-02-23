*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${url}     https://automationexercise.com/


*** Test Cases ***
Verify login scenerio with valid credentials
        Open Browser        ${url}      chrome
        #maximise the browser window
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        #wait untill the element
        Wait Until Element Is Visible    xpath://a[normalize-space()='Signup / Login']
        Click Element    xpath://a[normalize-space()='Signup / Login']
        Wait Until Element Is Visible    xpath://input[@data-qa='login-email']
        #enter the text in the username
        #Click Element    xpath://input[@type='text']
        Input Text    xpath://input[@data-qa='login-email']   ankitpatil@gmail.com
        Input Text    xpath://input[@placeholder='Password']  12345
        #click login button
        Click Element    xpath://button[normalize-space()='Login']
        #validate that the user is on the home page
        Wait Until Element Is Visible    xpath://li[10]//a[1]
        Element Text Should Be    xpath://a[contains(text(),'Logged in as')]    Logged in as ankit1

        Close Browser












