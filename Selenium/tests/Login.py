import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())

class Test_login:
    def test_login(self):
        driver = webdriver.Chrome(service=service)

        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        time.sleep(4)

        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")

        time.sleep(2)

        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        assert "OrangeHRM" in driver.title