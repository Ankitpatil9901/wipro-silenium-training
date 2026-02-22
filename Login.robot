*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${url}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login


*** Test Cases ***
Verify login scenerio with valid credentials
        Open Browser        ${url}      chrome
        #maximise the browser window
        Maximize Browser Window
        #wait untill the element 
        Wait Until Element Is Visible    xpath://div[@class='orangehrm-login-branding']
        #enter the text in the username
        Input Text    xpath://input[@placeholder='Username']   admin
        Input Text    xpath://input[@placeholder='Password']    admin123
        #click login button
        Click Element    xpath://button[@type= 'submit']
        #validate that the user is on the home page
        Wait Until Element Is Visible    xpath://div[@class='oxd-topbar-header-title']
        Element Should Be Visible    xpath//div[@class='oxd-topbar-header-title']

        Close Browser
