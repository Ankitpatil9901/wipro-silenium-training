#check the title of the web page
import time

import pytest

from Pages.Login_page import Loginpage


@pytest.mark.usefixtures("setup")
class TestLogin:

        def test_valid_login(self,driver):
            driver.get("https://opensource-demo.orangehrmlive.com/")
            time.sleep(3)
            lp = Loginpage(driver)
            lp.login("Admin","admin123")
            assert "Dashboard" in driver.title




