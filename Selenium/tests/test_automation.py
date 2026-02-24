#check the title of the web page
import time

import pytest
from selenium.webdriver.common.by import By
import os.path
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


from Pages.Login_page import Loginpage


@pytest.mark.usefixtures("driver")
class TestLogin:

        def test_valid_login(self,driver):
            driver.get("https://demowebshop.tricentis.com/login")
            time.sleep(3)

            # register
            reg=driver.find_element(By.XPATH,"//a[@class='ico-register']")
            reg.click()

            # registration form
            driver.find_element(By.XPATH, "//input[@id='gender-male']").click()
            driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys("Ankit")
            driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys("Patil")
            driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("ankit@gmail.com")
            driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("Test@1234")
            driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys("Test@1234")
            driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").click()
            time.sleep(2)

            #continue //input[@value='Continue']
            driver.find_element(By.XPATH, "//input[@value='Continue'").click()



