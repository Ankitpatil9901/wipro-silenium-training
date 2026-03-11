from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, by_locator):
        element = self.wait.until(
            EC.element_to_be_clickable(by_locator)
        )
        element.click()
    # for input fields
    def type(self, by_locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(by_locator)
        )
        element.clear()
        element.send_keys(text)
    # used to verify messages
    def get_text(self, by_locator):
        element = self.wait.until(
            EC.visibility_of_element_located(by_locator)
        )
        return element.text