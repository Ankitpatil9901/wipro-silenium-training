


import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_MultiSelectscrollradio:
    def test_multiscrollradio(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://testautomationpractice.blogspot.com/")
        element = driver.find_element(By.XPATH, "//input[@id='sunday']")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        checkbox_list= driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        count = len(checkbox_list)
        print(count)

        for i in checkbox_list:
            time.sleep(2)
            i.click()

        driver.close()