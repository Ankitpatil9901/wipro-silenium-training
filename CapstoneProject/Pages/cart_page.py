from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.Logger import get_logger

logger = get_logger()


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_checkout(self):

        try:
            self.click((By.XPATH, "//div[text()='Checkout']"))
            logger.info("Checkout button clicked")

        except Exception as e:
            logger.error(f"Cart checkout failed: {e}")
            raise