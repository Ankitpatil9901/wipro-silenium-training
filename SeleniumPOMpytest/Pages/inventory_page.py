from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_backpack = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        self.cart_icon = (By.XPATH, "//a[@class='shopping_cart_link']")

    def add_item_to_cart(self):
        self.driver.find_element(*self.add_backpack).click()

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()