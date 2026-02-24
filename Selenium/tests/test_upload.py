from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

from tests.Login import service

class Test_upload:
    def test_up(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/upload")
        time.sleep(2)

        browser = driver.find_element(By.XPATH,"//input[@id='file-upload']")
        browser.send_keys("C:\\Users\\Hp\\Downloads\\virat.webp")
        time.sleep(3)
        upload = driver.find_element(By.XPATH,"//input[@id='file-submit']")

        upload.click()
        time.sleep(3)
        fileupload = driver.find_element(By.XPATH,"//h3[normalize-space()='File Uploaded!']")
        assert fileupload.text == "File Uploaded!"

        time.sleep(3)
        driver.close()


