*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${url}     https://automationexercise.com/


*** Test Cases ***
Verify login scenerio with valid credentials
        #opening a browser
        Open Browser        ${url}      firefox
        #maximise the browser window
        Maximize Browser Window
        #setting the implicit wait for whole page
        Set Selenium Implicit Wait    5s
        #wait untill the element
        Wait Until Element Is Visible    xpath://a[normalize-space()='Signup / Login']
        #clicking on the sigup btn
        Click Element    xpath://a[normalize-space()='Signup / Login']
        Wait Until Element Is Visible    xpath://input[@placeholder='Name']
        #enter the text in the username
        #entering the name and email for signup
        Input Text    xpath://input[@placeholder='Name']   ankit1
        Input Text    xpath://input[@data-qa='signup-email']   patilankit2@gmail.com
        #click sign up button
        Click Element    xpath://button[normalize-space()='Signup']
        #choosing the gender
        Wait Until Element Is Visible    xpath://input[@id='id_gender1']
        Click Element    xpath://input[@id='id_gender1']
        # etering the password
        Input Text    xpath://input[@id='password']     12345
        # entering the dob
        Wait Until Element Is Visible    xpath://select[@id='days']
        ${labels}=      Get Selected List Label    xpath://select[@id='days']
        Log    ${labels}
        #select by label- visible text
        Select From List By Label    xpath://select[@id='days']     3
        Sleep    2s


        ${labels}=      Get Selected List Label    xpath://select[@id='months']
        Log    ${labels}
        #select by label- visible text
        Select From List By Label    xpath://select[@id='months']       April
        Sleep    2s

        ${labels}=      Get Selected List Label    xpath://select[@id='years']
        Log    ${labels}
        #select by label- visible text
        Select From List By Label    xpath://select[@id='years']    2002
        Sleep    2s
        # for checking the check box
        Click Element    xpath://input[@id='newsletter']
        Click Element    xpath://input[@id='optin']
        # entering the personal information
        Input Text    xpath://input[@id='first_name']    Ankit
        Input Text    xpath://input[@id='last_name']    Patil
        Input Text    xpath://input[@id='company']   wipro
        Input Text    xpath://input[@id='address1']    Sangameshwar Colony
        Input Text    xpath://input[@id='address2']    kalaburagi

        ${labels}=      Get Selected List Label    xpath://select[@id='country']
        Log    ${labels}
        #select by label- visible text
        Select From List By Label    xpath://select[@id='country']    India
        Sleep    2s


        Input Text    xpath://input[@id='state']    karnataka
        Input Text    xpath://input[@id='city']   Kalaburagi
        Input Text    xpath://input[@id='zipcode']   585103
        Input Text    xpath://input[@id='mobile_number']   1234123412
        #creating the account
        Click Element    xpath://button[normalize-space()='Create Account']
        Wait Until Element Is Visible    xpath://a[@class='btn btn-primary']
        Click Element    xpath://a[@class='btn btn-primary']
        Wait Until Element Is Visible    xpath://li[10]//a[1]
        Element Text Should Be    xpath://li[10]//a[1]     Logged in as ankit1
        Close Browser



*** Test Cases ***
2: Login User with correct email and password
        Open Browser        ${url}      firefox
        #maximise the browser window
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        #wait untill the element
        Wait Until Element Is Visible    xpath://a[normalize-space()='Signup / Login']
        Click Element    xpath://a[normalize-space()='Signup / Login']
        Wait Until Element Is Visible    xpath://input[@data-qa='login-email']
        #enter the text in the username
        #Click Element    xpath://input[@type='text']
        Input Text    xpath://input[@data-qa='login-email']   patilankit2@gmail.com
        Input Text    xpath://input[@placeholder='Password']  12345
        #click login button
        Click Element    xpath://button[normalize-space()='Login']
        #validate that the user is on the home page
        Wait Until Element Is Visible    xpath://li[10]//a[1]
        Element Text Should Be    xpath://a[contains(text(),'Logged in as')]    Logged in as ankit1

        Close Browser


*** Test Cases ***
3: Login User with incorrect email and passwords

        Open Browser        ${url}      firefox
        #maximise the browser window
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        #wait untill the element
        Wait Until Element Is Visible    xpath://a[normalize-space()='Signup / Login']
        #login
        Click Element    xpath://a[normalize-space()='Signup / Login']
        Wait Until Element Is Visible    xpath://input[@data-qa='login-email']
        #enter the text in the username
        #Click Element    xpath://input[@type='text']
        Input Text    xpath://input[@data-qa='login-email']   patil9@gmail.com
        Input Text    xpath://input[@placeholder='Password']  12385
        #click login button
        Click Element    xpath://button[normalize-space()='Login']
        Element Text Should Be    xpath://p[normalize-space()='Your email or password is incorrect!']    Your email or password is incorrect!
        Close Browser


*** Test Cases ***
4.Logout the user

        Open Browser        ${url}      firefox
        #maximise the browser window
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        #wait untill the element
        Wait Until Element Is Visible    xpath://a[normalize-space()='Signup / Login']
        Click Element    xpath://a[normalize-space()='Signup / Login']
        Wait Until Element Is Visible    xpath://input[@data-qa='login-email']
        #enter the text in the username
        #Click Element    xpath://input[@type='text']
        Input Text    xpath://input[@data-qa='login-email']   patilankit1@gmail.com
        Input Text    xpath://input[@placeholder='Password']  12345
        #click login button
        Click Element    xpath://button[normalize-space()='Login']
        Wait Until Element Is Visible    xpath://li[10]//a[1]
        Element Text Should Be    xpath://a[contains(text(),'Logged in as')]    Logged in as ankit1
        #logout
        Click Element    xpath://a[normalize-space()='Logout']
        Close Browser


*** Test Cases ***
5.Registering with the existing mail

        Open Browser        ${url}      firefox
        #maximise the browser window
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        #wait untill the element
        Wait Until Element Is Visible    xpath://a[normalize-space()='Signup / Login']
        Click Element    xpath://a[normalize-space()='Signup / Login']
        Wait Until Element Is Visible    xpath://input[@placeholder='Name']
        #enter the text in the username
        Input Text    xpath://input[@placeholder='Name']   ankit1
        Input Text    xpath://input[@data-qa='signup-email']   patilankit2@gmail.com
        #click login button
        Click Element    xpath://button[normalize-space()='Signup']
        Element Text Should Be    xpath://p[normalize-space()='Email Address already exist!']    Email Address already exist!
        Close Browser


*** Test Cases ***
6.Contact Us form

        Open Browser        ${url}      firefox
        #maximise the browser window
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        Wait Until Element Is Visible    xpath://a[normalize-space()='Contact us']
        Click Element    xpath://a[normalize-space()='Contact us']
        Element Text Should Be    //h2[normalize-space()='Get In Touch']    Get In Touch

        Input Text    xpath://input[@placeholder='Name']  ankit1
        Input Text    xpath://input[@placeholder='Email']   ankitpatil99@gmail.com
        Input Text    xpath://input[@placeholder='Subject']   Issue in login
        Input Text    xpath://textarea[@id='message']   Unable to login into m account
        Choose File    xpath://input[@name='upload_file']    "C:\Users\Hp\Downloads\virat.webp"

        Click Element    xpath://input[@name='submit']
        Handle Alert        action=ACCEPT       timeout=3

        
        Element Text Should Be    xpath://div[@class='status alert alert-success']    Success! Your details have been submitted successfully.
        Click Element    xpath://span[normalize-space()='Home']
        Element Should Be Visible    xpath://img[@alt='Website for automation practice']
        Close Browser



*** Test Cases ***
7. Test cases Validation
        Open Browser        ${url}      firefox
        #maximise the browser window
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        #wait untill the element
        Wait Until Element Is Visible    xpath://a[normalize-space()='Signup / Login']
        Click Element    xpath://a[normalize-space()='Test Cases']//i[@class='fa fa-list']
        Element Should Be Visible    xpath://b[contains(text(),'Test Cases')]
        Close Browser


*** Test Cases ***
8: Verify All Products and product detail page
        Open Browser        ${url}      firefox
        #maximise the browser window
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        #wait untill the element
        Wait Until Element Is Visible    xpath://a[normalize-space()='Signup / Login']
        
        Click Element    xpath://a[@href='/products']

        Element Should Be Visible    xpath://h2[normalize-space()='All Products']
        Element Should Be Visible    xpath://div[@class='brands_products']
        Sleep    3s
        Wait Until Element Is Visible    xpath://a[@href='/product_details/1']
        Sleep    3s
        Click Element    xpath://a[@href='/product_details/1']
        Element Should Be Visible    xpath://div[@class='product-information']
        Close Browser

*** Test Cases ***
9: Search Product

        Open Browser        ${url}      firefox
        #maximise the browser window
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        #wait untill the element
        Wait Until Element Is Visible    xpath://a[normalize-space()='Signup / Login']

        Click Element    xpath://a[@href='/products']

        Element Should Be Visible    xpath://h2[normalize-space()='All Products']
        Input Text    xpath://input[@id='search_product']    Polo
        Click Element    xpath://button[@id='submit_search']
        Mouse Over    xpath://div[@class='product-image-wrapper']
        Element Should Contain    xpath://div[@class='overlay-content']//p    Polo
        Close Browser


*** Test Cases ***
10: Verify Subscription in home page

        Open Browser        ${url}      firefox
        #maximise the browser window
        Maximize Browser Window
        Set Selenium Implicit Wait    5s
        #wait untill the element
        Wait Until Element Is Visible    xpath://a[normalize-space()='Signup / Login']

        Scroll Element Into View    xpath://h2[normalize-space()='Subscription']
        Input Text    xpath://input[@id='susbscribe_email']    patilankit2@gmail.com
        Click Element    xpath://i[@class='fa fa-arrow-circle-o-right']
        Alert Should Be Present    You have been successfully subscribed!
        Close Browser