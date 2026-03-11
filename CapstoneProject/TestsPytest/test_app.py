import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage
from utilities.excel_utils import ExcelUtils
from utilities.Logger import get_logger

logger = get_logger()
excel_path = "C:\\Users\\Hp\\PycharmProjects\\Selenium_Project_POM\\test_data\\testdata.xlsx"

# 1 Test Login
def test_login(setup):
    driver = setup
    logger.info("Starting Login Test")
    try:
        username, password = ExcelUtils.read_login_data(excel_path)
        logger.info("Read login data from Excel")
        login = LoginPage(driver)
        login.click_signin()
        logger.info("Entering login credentials")
        login.login(username, password)
        logger.info("Login Test Completed Successfully")
    except Exception as e:
        logger.error(f"Login Test Failed: {e}")
        pytest.fail("Login test failed")

# 2 Login + Inventory Search
def test_login_and_inventory(setup):
    driver = setup
    logger.info("Starting Login + Inventory Test")
    try:
        username, password = ExcelUtils.read_login_data(excel_path)
        product = ExcelUtils.read_product_data(excel_path)
        login = LoginPage(driver)
        login.click_signin()
        login.login(username, password)
        logger.info("Login successful")

        inventory = InventoryPage(driver)
        logger.info("Searching product: iPhone 12")
        inventory.search_product(product)

        logger.info("Inventory search test completed")
    except Exception as e:
        logger.error(f"Inventory Test Failed: {e}")
        pytest.fail("Inventory test failed")

# 3 Login + Inventory + Add to Cart
def test_add_product_to_cart(setup):
    driver = setup
    logger.info("Starting Add Product to Cart Test")
    try:
        username, password = ExcelUtils.read_login_data(excel_path)
        product = ExcelUtils.read_product_data(excel_path)

        login = LoginPage(driver)
        login.click_signin()
        login.login(username, password)
        logger.info("Login successful")

        inventory = InventoryPage(driver)
        inventory.search_product(product)
        logger.info("Product searched")

        inventory.add_product_to_cart(product)
        logger.info("Product added to cart")
    except Exception as e:
        logger.error(f"Add to Cart Test Failed: {e}")
        pytest.fail("Add to cart test failed")

# 4 Login + Inventory + Cart + Checkout
def test_checkout_process(setup):
    driver = setup
    logger.info("Starting Checkout Process Test")

    try:
        username, password = ExcelUtils.read_login_data(excel_path)
        product = ExcelUtils.read_product_data(excel_path)

        login = LoginPage(driver)
        login.click_signin()
        login.login(username, password)
        logger.info("Login successful")

        inventory = InventoryPage(driver)
        inventory.search_product(product)
        inventory.add_product_to_cart(product)
        logger.info("Product added to cart")

        inventory.go_to_cart()
        logger.info("Navigated to cart page")

        inventory.check_out()
        cart = CartPage(driver)
        cart.click_checkout()
        logger.info("Checkout clicked")

    except Exception as e:
        logger.error(f"Checkout Process Failed: {e}")
        pytest.fail("Checkout process test failed")


# 5 Complete Order Flow
def test_complete_flow(setup):
    driver = setup
    logger.info("Starting Complete Order Flow Test")

    try:
        username, password = ExcelUtils.read_login_data(excel_path)
        product = ExcelUtils.read_product_data(excel_path)
        fname, lname, address, state, postal = ExcelUtils.read_shipping_data(excel_path)

        login = LoginPage(driver)
        login.click_signin()
        login.login(username, password)
        logger.info("Login successful")

        inventory = InventoryPage(driver)
        inventory.search_product(product)
        inventory.add_product_to_cart(product)
        logger.info("Product added to cart")

        inventory.go_to_cart()
        inventory.check_out()

        cart = CartPage(driver)
        cart.click_checkout()
        logger.info("Moved to checkout page")

        checkout = CheckoutPage(driver)
        checkout.fill_shipping_details(fname, lname, address, state, postal)
        logger.info("Shipping details entered")

        confirm = ConfirmationPage(driver)

        logger.info("Verifying order success message")
        assert "successfully placed" in confirm.verify_success_message()

        confirm.download_receipt()
        logger.info("Downloading receipt")

        assert confirm.verify_download()
        logger.info("Receipt downloaded successfully")

        logger.info("Complete Order Flow Test Passed")

    except Exception as e:
        logger.error(f"Complete Flow Test Failed: {e}")
        print("Actual error ",e)
        pytest.fail("Complete order flow test failed")