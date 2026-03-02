from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SelectMenuPage:
    """Page Object Model for jQuery UI Selectmenu demo"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def switch_to_demo_iframe(self):
        """Switch into the demo iframe"""
        iframe = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".demo-frame")))
        self.driver.switch_to.frame(iframe)

    def select_option(self, button_id, option_text, menu_id=None):
        """
        Select an option from a jQuery UI dropdown
        :param button_id: ID of the dropdown button (e.g., 'speed-button')
        :param option_text: Visible text of option (e.g., 'Fast')
        :param menu_id: Optional dropdown menu ID; auto-calculated if None
        """
        # Click the dropdown button
        button = self.wait.until(EC.element_to_be_clickable((By.ID, button_id)))
        button.click()

        if not menu_id:
            menu_id = button_id.replace("-button", "-menu")

        # Click the desired option
        option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//ul[@id='{menu_id}']//div[text()='{option_text}']"))
        )
        option.click()
        time.sleep(0.5)  # small pause to ensure selection completes