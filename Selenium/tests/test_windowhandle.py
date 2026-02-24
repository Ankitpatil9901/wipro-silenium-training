import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

class Test_window:
    def test_win(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/windows")
        driver.maximize_window()
        time.sleep(2)
        driver.implicitly_wait(10)

        clickhere = driver.find_element(By.XPATH, "//a[normalize-space()='Click Here']")
        clickhere.click()

        windows = driver.window_handles
        print(windows)

        driver.switch_to.window(windows[1])

        text = driver.find_element(By.XPATH, "//h3[contains(text(),'New Window')]")
        print(text.text)

        driver.close()

        driver.switch_to.window(windows[0])
        clickhere.is_displayed()

        driver.close()