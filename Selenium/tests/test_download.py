import os.path

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

from tests.Login import service

DOWN_dir = "C:\\Users\\Hp\\Downloads"

class Test_download:
    def test_down(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        driver.get("https://the-internet.herokuapp.com/download")
        driver.maximize_window()
        time.sleep(2)

        alert = driver.find_element(By.XPATH,"//a[normalize-space()='alert.jpeg']")
        alert.click()

        file_path= os.path.join(DOWN_dir,"alert.jpeg")
        assert os.path.exists(file_path)


        time.sleep(3)
        driver.close()


