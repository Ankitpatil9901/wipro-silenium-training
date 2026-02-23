#Selecting by visible text
#Selecting by indexing
#Selecting the value

*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php



*** Test Cases ***
Verify drop downs
        Open Browser        ${url}      firefox
        #maximise the browser window
        Maximize Browser Window
        Wait Until Element Is Visible    //select[@id='state']
        ${labels}=      Get Selected List Label    //select[@id='state']
        Log    ${labels}
        #select by label- visible text
        Select From List By Label    id=state      Uttar Pradesh
        Sleep    2s
        #select by label- visible text
        Select From List By Label    id=city      Lucknow
        Sleep    2s


        Close Browser




