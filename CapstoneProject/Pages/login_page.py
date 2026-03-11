from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.Logger import get_logger

logger = get_logger()


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_signin(self):

        try:
            self.click((By.ID, "signin"))
            logger.info("Clicked Sign In button")

        except Exception as e:
            logger.error(f"Error clicking Sign In: {e}")
            raise

    def login(self, username, password):

        try:
            self.click((By.ID, "username"))
            self.click((By.XPATH, f"//div[text()='{username}']"))

            self.click((By.ID, "password"))
            self.click((By.XPATH, f"//div[text()='{password}']"))

            self.click((By.ID, "login-btn"))

            logger.info("Login completed")

        except Exception as e:
            logger.error(f"Login failed: {e}")
            raise