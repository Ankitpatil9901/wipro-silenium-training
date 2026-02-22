*** Settings ***
#settings add the external library details , resources , setup and teardown commands
Library     SeleniumLibrary

*** Test Cases ***
#name of the testcase
Verify login with valid credentials
    Log     Enter usernamr
    Log     Enter password
    Log     click on login button
    Log     user is on th home page

