import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_automationpractice:

    def test_full_flow(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        driver.implicitly_wait(5)

        # Open window and close
        driver.find_element(By.XPATH, "//button[@id='openwindow']").click()
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        # Open tab and close
        driver.find_element(By.XPATH, "//a[@id='opentab']").click()
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        # Scroll down
        driver.execute_script("window.scrollBy(0,700)")
        time.sleep(2)

        # Second table – Chennai
        rows = driver.find_elements(By.XPATH, "//table[@id='product']/tbody/tr")
        for r in rows:
            if "Chennai" in r.text:
                print(r.text)

        # First table – Advanced Selenium Framework
        cell = driver.find_element(By.XPATH, "//table[@name='courses']/tbody/tr[10]/td[2]")

        print(cell.text)
        # Mouse hover → Top
        hover = driver.find_element(By.XPATH, "//button[@id='mousehover']")
        ActionChains(driver).move_to_element(hover).perform()
        driver.find_element(By.LINK_TEXT, "Top").click()
        assert driver.current_url == "https://rahulshettyacademy.com/AutomationPractice/#top"

        # Iframe – extract text
        driver.switch_to.frame("courses-iframe")
        print(driver.find_element(By.TAG_NAME, "body").text)
        driver.switch_to.default_content()

        driver.close()