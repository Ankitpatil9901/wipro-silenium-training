*** Settings ***
#settings add the external library details , resources , setup and teardown commands
Library     SeleniumLibrary
Resource        ./../Resource/Resource.robot
Suite Setup     Open DB
Suite Teardown      Log     Close DB

*** Test Cases ***
#name of the testcase
Verify login with valid credentials
                Login

Verify login with valid credentials

    Log     User selects the product
    Log     User add the product to the cart
    Log     user verifies the product with details

