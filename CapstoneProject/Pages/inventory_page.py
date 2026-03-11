from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.Logger import get_logger

logger = get_logger()

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    def search_product(self, product_name):
        try:
            self.type((By.XPATH, "//input[@placeholder='Search']"), product_name)

            self.click((By.XPATH, "//button[@role='button']"))

            logger.info(f"Product searched: {product_name}")

        except Exception as e:
            logger.error(f"Search product failed: {e}")
            raise

    def add_product_to_cart(self, product_name):

        try:
            self.click((
                By.XPATH,
                f"//p[text()='{product_name}']/ancestor::div[contains(@class,'shelf-item')]//div[text()='Add to cart']"
            ))

            logger.info("Product added to cart")

        except Exception as e:
            logger.error(f"Add to cart failed: {e}")
            raise

    def go_to_cart(self):

        try:
            self.click((By.XPATH, "//span[contains(@class,'bag')]"))
            logger.info("Navigated to cart")

        except Exception as e:
            logger.error(f"Failed to open cart: {e}")
            raise

    def check_out(self):

        try:
            self.click((By.XPATH, "//div[@class='buy-btn']"))
            logger.info("Checkout clicked")

        except Exception as e:
            logger.error(f"Checkout failed: {e}")
            raise