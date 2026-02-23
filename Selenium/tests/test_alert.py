import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_radio:
    def test_radio(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        time.sleep(2)
        #simple alert
        simplealert = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']")
        simplealert.click()

        alert = driver.switch_to.alert
        alert.accept() # click on ok
        time.sleep(2)

        # confirmational alert
        confalert = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
        confalert.click()

        alert = driver.switch_to.alert
        alert.dismiss() #click on cancel
        time.sleep(2)

        # prompt alert
        promalert = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
        promalert.click()
        alt = driver.switch_to.alert

        alerttext = alt.text
        print(alerttext)
        alt.send_keys("testhello")
        time.sleep(2)
        alt.accept()

        driver.quit()