import pytest
from selenium import webdriver
from pages.login_page1 import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutInfoPage
from pages.checkoutoverview_page import CheckoutOverviewPage
from pages.confirmation_page import ConfirmationPage
from utilities.excel_utils import get_excel_data
from utilities.Logger import get_logger


logger = get_logger()
test_data = get_excel_data("C:/Users/Hp/PycharmProjects/SeleniumPytestPOM/test_data/login_data.xlsx","Sheet1")

class TestSwagLabs:

    @pytest.mark.parametrize("user, password", test_data)
    def test_complete_purchase_flow(self, driver, user, password):
        logger.info("Opening the application")
        #Login
        driver.get("https://www.saucedemo.com/")
        login = LoginPage(driver)
        logger.info("entering the credentials")
        login.login(user,password)
        

        #Add to Cart
        inventory = InventoryPage(driver)
        inventory.add_item_to_cart()
        inventory.open_cart()

        #Checkout
        cart = CartPage(driver)
        cart.click_checkout()

        #Enter Info
        info = CheckoutInfoPage(driver)
        logger.info("entering the personal details")
        info.enter_info("Ankit", "Patil", "12345")

        #Finish
        overview = CheckoutOverviewPage(driver)
        overview.click_finish()

        #Verify Text and Go Home
        confirm = ConfirmationPage(driver)
        assert "Thank you for your order!" in confirm.get_confirmation_text()

        confirm.go_back_home()

        # Verification
        # screenshot if a testcase fails
        assert "inventory.html" in driver.current_url

        driver.close()