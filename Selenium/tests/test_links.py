import os.path
from itertools import count

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

        links = driver.find_elements(By.TAG_NAME,"a")
        count = len(links)
        print(count)

        for link in links:
            print(link.text)


        time.sleep(3)
        driver.close()


