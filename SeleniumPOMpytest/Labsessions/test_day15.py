import pytest
from selenium import webdriver
from pages.day15 import SelectMenuPage


@pytest.fixture
def driver():
    """Initialize Chrome WebDriver and quit after test"""
    driver = webdriver.Chrome()  # Make sure chromedriver is in PATH
    driver.maximize_window()
    yield driver
    driver.quit()


def test_select_speed_file_number(driver):
    """Test selecting options from all dropdowns"""
    driver.get("https://jqueryui.com/selectmenu/")
    page = SelectMenuPage(driver)

    # Switch to demo iframe
    page.switch_to_demo_iframe()

    # Select options
    page.select_option("speed-button", "Fast")
    page.select_option("files-button", "ui.jQuery.js")
    page.select_option("number-button", "10")