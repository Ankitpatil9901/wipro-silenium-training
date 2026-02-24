from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestDatePicker:
    def test_select_date(self, driver):
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            driver.maximize_window()
            driver.get("https://rsuitejs.com/components/date-picker/")   # example page
            wait = WebDriverWait(driver, 10)

            # open date picker
            date_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[4]//div[1]//div[1]//div[1]//div[1]//span[1]//*[name()='svg']")))
            date_input.click()

            # select month/year if needed (already Feb 2026 in your screenshot)

            # select day = 24
            day = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='25']")))
            day.click()

            time.sleep(3)
            driver.quit()