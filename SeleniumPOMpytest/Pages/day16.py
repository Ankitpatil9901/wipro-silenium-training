from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CarsPage:
    """Page Object Model for PHP Travels Cars page"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_pickup_location(self, location_text):
        pickup = self.wait.until(EC.element_to_be_clickable((By.ID, "pickuplocation")))
        pickup.clear()
        pickup.send_keys(location_text)

        # select first suggestion
        suggestion = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(@class,'select2-results__option')]"))
        )
        suggestion.click()

    def enter_dropoff_location(self, location_text):
        dropoff = self.wait.until(EC.element_to_be_clickable((By.ID, "dropofflocation")))
        dropoff.clear()
        dropoff.send_keys(location_text)

        # select first suggestion
        suggestion = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(@class,'select2-results__option')]"))
        )
        suggestion.click()

    def enter_pickup_date(self, date_text):
        pickup_date = self.wait.until(EC.element_to_be_clickable((By.ID, "pickupdate")))
        pickup_date.clear()
        pickup_date.send_keys(date_text)

    def enter_dropoff_date(self, date_text):
        dropoff_date = self.wait.until(EC.element_to_be_clickable((By.ID, "dropoffdate")))
        dropoff_date.clear()
        dropoff_date.send_keys(date_text)

    def click_search(self):
        search_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Search')]"))
        )
        search_btn.click()

    def select_first_car(self):
        first_car = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'car-listing')])[1]"))
        )
        first_car.click()