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

        driver.get("https://trytestingthis.netlify.app/")
        driver.maximize_window()
        time.sleep(2)

        title = driver.title
        print(title)

        url = driver.current_url
        print(url)
        time.sleep(3)

        driver.back()

        time.sleep(3)

        driver.forward()
        time.sleep(3)

        driver.refresh()
        driver.close()


