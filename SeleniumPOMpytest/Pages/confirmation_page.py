from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.complete_header = (By.XPATH, "//div[@id='checkout_complete_container']")
        self.back_home_button = (By.XPATH, "//button[@id='back-to-products']")

    def get_confirmation_text(self):
        return self.driver.find_element(*self.complete_header).text

    def go_back_home(self):
        self.driver.find_element(*self.back_home_button).click()
        self.wait.until(EC.url_contains("inventory.html"))