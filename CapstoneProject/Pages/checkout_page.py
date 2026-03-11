import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.Logger import get_logger

logger = get_logger()


class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_shipping_details(self, firstname, lastname, address, state, postalcode):

        try:
            self.type((By.ID, "firstNameInput"), firstname)
            self.type((By.ID, "lastNameInput"), lastname)
            self.type((By.ID, "addressLine1Input"), address)
            self.type((By.ID, "provinceInput"), state)
            self.type((By.ID, "postCodeInput"), postalcode)
            time.sleep(3)

            self.click((By.ID, "checkout-shipping-continue"))

            logger.info("Shipping details entered")

        except Exception as e:
            logger.error(f"Shipping details failed: {e}")
            raise

