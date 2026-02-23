*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${url}    https://practice.automationtesting.in/


*** Test Cases ***
Verify Ecommerce
        Open Browser        ${url}      chrome
        #maximise the browser window
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        #wait untill the element
        Wait Until Element Is Visible    xpath://img[@alt='Shop Selenium Books']

        Scroll Element Into View    xpath://img[@title='Selenium Ruby']
        #enter the text in the username
        #Input Text    xpath://input[@id='user-name']   standard_user
        #Input Text    xpath://input[@id='password']    secret_sauce
        #click login button
        #Click Element    xpath://input[@id='login-button']
        #validate that the user is on the home page
        #Wait Until Element Is Visible    xpath://button[@id='add-to-cart-sauce-labs-backpack']
        #Element Should Be Visible    xpath://button[@id='add-to-cart-sauce-labs-backpack']
        #add to cart
        Click Element    xpath://li[@class='post-160 product type-product status-publish has-post-thumbnail product_cat-selenium product_tag-ruby product_tag-selenium has-post-title no-post-date has-post-category has-post-tag has-post-comment has-post-author first instock downloadable taxable shipping-taxable purchasable product-type-simple']//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'][normalize-space()='Add to basket']
        #check the cart
        Click Element    xpath://a[@class='added_to_cart wc-forward']
        # verifying the cart
        #Wait Until Element Is Visible    xpath://div[@class='inventory_item_name']
        #Element Should Be Visible    xpath://div[@class='inventory_item_name']

        #Checkout
        #Click Element    xpath://button[@id='checkout']

        #adding details
        #Input Text    xpath://input[@id='first-name']  Ankit
        #Input Text    xpath://input[@id='last-name']  Patil
        #Input Text    xpath://input[@id='postal-code']  585103
        #Click Element    xpath://input[@id='continue']


        #Confirming the items
        #Wait Until Element Is Visible    xpath://button[@id='finish']
        #Element Should Be Visible    xpath://button[@id='finish']
        #Click Element    xpath://button[@id='finish']

        #verifying the last page

        #Page Should Contain    Thank you for your order!













