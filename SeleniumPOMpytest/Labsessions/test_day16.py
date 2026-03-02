import pytest
from selenium import webdriver
from pages.day16 import CarsPage

@pytest.fixture
def driver():
    """Initialize Chrome WebDriver and quit after test"""
    driver = webdriver.Chrome()  # make sure chromedriver is in PATH
    driver.maximize_window()
    yield driver
    driver.quit()

def test_php_travels_car_booking(driver):
    """Test car booking search on PHP Travels"""
    driver.get("https://phptravels.net/cars")
    cars_page = CarsPage(driver)

    # Enter pickup & dropoff
    cars_page.enter_pickup_location("New York")
    cars_page.enter_dropoff_location("Los Angeles")

    # Enter pickup & dropoff dates
    cars_page.enter_pickup_date("10/15/2026")
    cars_page.enter_dropoff_date("10/20/2026")

    # Click search
    cars_page.click_search()

    # Optionally select first car
    cars_page.select_first_car()