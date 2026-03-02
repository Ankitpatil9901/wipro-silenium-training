import pytest
from selenium import webdriver
from pages.day15a import MenuPage

@pytest.fixture
def driver():
    """Initialize Chrome WebDriver and quit after test"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_select_electronics_carhifi(driver):
    """Test selecting Electronics → Car Hifi from menu"""
    driver.get("https://jqueryui.com/menu/")
    menu_page = MenuPage(driver)

    # Switch to iframe
    menu_page.switch_to_demo_iframe()

    # Select menu and submenu
    menu_page.select_menu("Electronics", "Car Hifi")