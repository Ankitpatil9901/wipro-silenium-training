from selenium.webdriver.common.by import By

class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver
        self.finish_button = (By.XPATH, "//button[@id='finish']")

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()