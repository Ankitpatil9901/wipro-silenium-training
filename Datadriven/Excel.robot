*** Settings ***
Library     SeleniumLibrary
Library     DataDriver      file=C:/Users/Hp/PycharmProjects/wiproRobotfw/Testdata/ddtLogindata.xlsx     sheet_name=ddtLogindata
#test template provide a data-driven approach to testing a single keyword
#

Test Template       Login Test
Test Setup     Open Browser        https://opensource-demo.orangehrmlive.com/web/index.php/auth/login      firefox
Test Teardown      Close Browser

*** Test Cases ***
Login with user     ${username} and         ${password}


*** Keywords ***
Login Test
        [Arguments]     ${username}     ${password}
        Wait Until Element Is Visible    xpath://input[@placeholder='Username']
        #enter the usename
        Input Text    xpath://input[@placeholder='Username']   ${username}
        #enter the password
        Input Text    xpath://input[@placeholder='Password']    ${password}
        #click thelogin btn
        Click Element    xpath://button[@type='submit']

        Wait Until Element Is Visible    xpath://div[@class='oxd-topbar-header-title']
        Element Should Be Visible    xpath://div[@class='oxd-topbar-header-title']

        Close Browser



