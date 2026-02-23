'''
'''
'''
locators = Page actions

reusability ,
easy maintainece
readability


logon page
1. verify login with valid credentials
2. verify login with invalid credentials
3.Verify password masking
4.Verify with blank credentials
5.Verify input text field validation
6 Verify password field allowance
7. verify logo of the login page
'''
'''
'''

from selenium.webdriver.common.by import By
class Loginpage:

        #locators
        username_input = (By.NAME, "username")
        password_input = (By.NAME, "password")
        login_button= (By.XPATH,"//button[normalize-space()='Login']")
        dashboard_text = (By.XPATH,"//h6[normalize-space()='Dashboard']")

        def __init__(self,driver):
            self.driver = driver

        def enter_username(self,username):
            self.driver.findelement(self.username_input).send_keys(username)

        def enter_password(self,password):
            self.driver.findelement(self.password_input).send_keys(password)

        def click_login(self):
            self.driver.findelement(self.login_button).click()

        def login(self, username, password):
            self.enter_username(username)
            self.enter_password(password)
            self.click_login()

