import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def test_banking_flow(driver):
    wait = WebDriverWait(driver, 10)
    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

    # Open URL
    driver.get(url)

    # Customer Login
    customer_login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Customer Login']")))
    customer_login_btn.click()

    # Select User
    user_select_element = wait.until(EC.visibility_of_element_located((By.ID, "userSelect")))
    dropdown = Select(user_select_element)
    dropdown.select_by_visible_text("Albus Dumbledore")

    # Click Login
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(3)

    # Verify Welcome Message
    wait.until(EC.presence_of_element_located((By.XPATH, "//strong[contains(text(),'Welcome')]")))

    # Deposit Logic
    driver.find_element(By.XPATH, "//button[contains(.,'Deposit')]").click()
    amount_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='amount']")))
    amount_input.send_keys("100000")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Verify Deposit
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Deposit Successful']")))

    # Withdrawal Logic
    driver.find_element(By.XPATH, "//button[contains(.,'Withdrawl')]").click()

    # Wait for the label to switch from Deposit to Withdrawal to avoid "Stale Element"
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//label"), "Amount to be Withdrawn :"))

    driver.find_element(By.XPATH, "//input[@placeholder='amount']").send_keys("1000")
    driver.find_element(By.XPATH, "//button[text()='Withdraw']").click()

    # Final Validations
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Transaction successful']")))

    # Verify Balance
    balance_element = driver.find_element(By.XPATH, "//div[@class='center']/strong[2]")
    assert balance_element.text == "99000", f"Expected balance 99000 but got {balance_element.text}"

    # Logout
    driver.find_element(By.XPATH, "//button[text()='Logout']").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='box mainhdr']")))

    driver.close()