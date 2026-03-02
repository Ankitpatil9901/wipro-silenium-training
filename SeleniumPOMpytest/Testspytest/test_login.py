import time
import pytest
from pages.Login_page import LoginPage
from utilities.Logger import get_logger
from utilities.excel_utils import get_excel_data

logger = get_logger()
test_data = get_excel_data("C:/Users/Hp/PycharmProjects/SeleniumPytestPOM/test_data/login_data.xlsx","Sheet1")

class TestLogin:
    def test_valid_login(self,driver):
        logger.info("Opening the application")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        #create the object of login page
        #class of the page has to be used
        lp = LoginPage(driver)
        logger.info("entering the credentials")
        lp.login("Admin","admin123")

        time.sleep(3)
        assert "OrangeHRM" in driver.title

    def test_invalid_login(self,driver):
        logger.info("Opening the application")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        #create the object of login page
        #class of the page has to beused
        lp = LoginPage(driver)
        logger.info("entering the credentials")
        lp.login("Admin","admin12345")

        time.sleep(3)
        assert "Invalid credentials" in lp.get_error_message()
    @pytest.mark.parametrize("username, password", test_data)
    def test_test_login_excel(self,driver,username,password):
        logger.info("Opening the application")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        lp = LoginPage(driver)
        lp.login(username, password)

        if password == "admin123":
            assert "OrangeHRM" in driver.title
        else:
            assert "Invalid credentials" in lp.get_error_message()


# for parallel execution pytest test_login.py -n 3

