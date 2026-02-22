*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${url}      https://rahulshettyacademy.com/AutomationPractice/


*** Test Cases ***
Verify multiselect check box
        Open Browser        ${url}      chrome
        #maximise the browser window
        Maximize Browser Window
        #idntify the common elements attribute -//input[@type = 'checkbox']
        ${elements}=        Get WebElements    xpath://input[@type = 'checkbox']
        FOR    ${element}    IN    @{elements}
            Click Element    ${element}
            Sleep    2s
        END
        Close Browser
