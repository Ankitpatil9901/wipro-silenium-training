from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestWaits:
    def test_wait(self, driver):
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            driver.maximize_window()
            driver.get("https://rsuitejs.com/components/date-picker/")
            driver.maximize_window()
            wait = WebDriverWait(driver, 10)

            # implicit waits -- This is globalcall it will apply to every element call for the entire session
            driver.implicitly_wait(2)

            #explicit wait
            radio_btn = driver.find_element(By.XPATH, "(//input[@value = 'radio2'])[1]")
            wait = WebDriverWait(driver,timeout=2)
            wait.until(lambda :radio_btn.is_displayed())

            # custom wait for fluent wait
            errors = [NoSuchElementException, ElementNotInteractableException]
            wait = WebDriverWait(driver, timeout=2, poll_frequency=2, ignored_exceptions=errors)
            wait.until(lambda :radio_btn.send_keys("Displayed") or True)
            time.sleep(3)
            driver.close()