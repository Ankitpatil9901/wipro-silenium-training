*** Settings ***
#settings add the external library details , resources , setup and teardown commands
Library     SeleniumLibrary

*** Test Cases ***
#name of the testcase
Verify login with valid credentials
                Login

Verify login with valid credentials

    Log     User selects the product
    Log     User add the product to the cart
    Log     user verifies the product with details

*** Keywords ***
Login

    Log     Enter usernamr
    Log     Enter password
    Log     click on login button
    Log     user is on th home page

