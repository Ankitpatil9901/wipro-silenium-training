*** Settings ***
# run --  robot .\Testcase1.robot
#Log to console - will display on console
#Log - will display in the reporty
#settings add the external library details , resources , setup and teardown commands
Library     SeleniumLibrary

*** Test Cases ***
#name of the testcase
Verify login with valid credentials
    Log To Console     Enter usernamr
    Log To Console    Enter password
    Log To Console   click on login button
    Log To Console     user is on th home page