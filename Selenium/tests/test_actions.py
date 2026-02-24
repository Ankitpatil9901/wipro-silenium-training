from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

from tests.Login import service

class Test_actions:
    def test_action(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.amazon.in/")
        time.sleep(2)

        actions = ActionChains(driver)
        bestsellers = driver.find_element(By.XPATH,"//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
        # double click using actions class
        actions.double_click(bestsellers).perform()#double click
        time.sleep(3)
        driver.back()
        time.sleep(3)

        mobiles = driver.find_element(By.XPATH,"//a[normalize-space()='Mobiles']")
        actions = ActionChains(driver)
        actions.click(mobiles).perform()# right click
        time.sleep(3)
        driver.back()


        #move to element
        prime = driver.find_element(By.XPATH,"//span[normalize-space()='Prime']")
        actions.move_to_element(prime).perform()

        #click and hold
        fresh = driver.find_element(By.XPATH, "//span[normalize-space()='Fresh']")
        actions.click_and_hold(fresh).perform()

        driver.close()




