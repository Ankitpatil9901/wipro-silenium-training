from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutInfoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.first_name = (By.XPATH, "//input[@id='first-name']")
        self.last_name = (By.XPATH, "//input[@id='last-name']")
        self.zip_code = (By.XPATH, "//input[@id='postal-code']")
        self.continue_button = (By.XPATH, "//input[@id='continue']")

    def enter_info(self, fname, lname, zip_code):
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.zip_code).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()