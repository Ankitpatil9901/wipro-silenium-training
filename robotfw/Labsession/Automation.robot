*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${url}     https://www.saucedemo.com/


*** Test Cases ***
Verify login scenerio with valid credentials
        Open Browser        ${url}      chrome
        #maximise the browser window
        Maximize Browser Window
        #wait untill the element
        Wait Until Element Is Visible    xpath://input[@id='user-name']
        #enter the text in the username
        Input Text    xpath://input[@id='user-name']   standard_user
        Input Text    xpath://input[@id='password']    secret_sauce
        #click login button
        Click Element    xpath://input[@id='login-button']
        #validate that the user is on the home page
        Wait Until Element Is Visible    xpath://button[@id='add-to-cart-sauce-labs-backpack']
        Element Should Be Visible    xpath://button[@id='add-to-cart-sauce-labs-backpack']
        #add to cart
        Click Element    xpath://button[@id='add-to-cart-sauce-labs-backpack']
        #check the cart
        Click Element    xpath://a[@class='shopping_cart_link']
        # verifying the cart
        Wait Until Element Is Visible    xpath://div[@class='inventory_item_name']
        Element Should Be Visible    xpath://div[@class='inventory_item_name']

        #Checkout
        Click Element    xpath://button[@id='checkout']

        #adding details
        Input Text    xpath://input[@id='first-name']  Ankit
        Input Text    xpath://input[@id='last-name']  Patil
        Input Text    xpath://input[@id='postal-code']  585103
        Click Element    xpath://input[@id='continue']


        #Confirming the items
        Wait Until Element Is Visible    xpath://button[@id='finish']
        Element Should Be Visible    xpath://button[@id='finish']
        Click Element    xpath://button[@id='finish']

        #verifying the last page

        Page Should Contain    Thank you for your order!













