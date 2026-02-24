import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

class Test_webtb:
    def test_table(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/tables")
        driver.maximize_window()
        time.sleep(2)
        driver.implicitly_wait(10)

        #tr- row
        #td - column
        #th - header

        #num of rows
        rows = driver.find_elements(By.XPATH,"//table[@id = 'table1']/tbody/tr")
        for i in rows:
            print(i.text)

        time.sleep(2)

        # num of columns
        cols = driver.find_elements(By.XPATH, "//table[@id = 'table1']/tbody/tr[1]/td")
        for i in cols:
            print(i.text)

        time.sleep(3)
        #fetch the cell data

        celldata = driver.find_element(By.XPATH,"//table[@id = 'table1']/tbody/tr[1]/td[4]")
        assert "$50.00" in celldata.text
        driver.close()
