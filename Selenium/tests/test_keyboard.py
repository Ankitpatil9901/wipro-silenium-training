from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

class Test_keyboard:
    def test_kb(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.facebook.com/")
        time.sleep(2)

        email = driver.find_element(By.NAME, "email")
        password = driver.find_element(By.NAME, "pass")

        # type HELLO
        ActionChains(driver).click(email)\
            .key_down(Keys.SHIFT).send_keys("hello").key_up(Keys.SHIFT).perform()

        # CTRL + A
        ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

        # CTRL + C
        ActionChains(driver).key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

        # CTRL + V into password
        ActionChains(driver).click(password)\
            .key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

        # show password click
        show_pwd = driver.find_element(By.XPATH, "//div[@aria-label='Show password']")
        show_pwd.click()

        time.sleep(3)
        driver.quit()