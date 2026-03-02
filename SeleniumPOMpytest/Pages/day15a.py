from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MenuPage:
    """Page Object Model for jQuery UI Menu demo"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    def switch_to_demo_iframe(self):
        """Switch into the demo iframe"""
        iframe = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".demo-frame")))
        self.driver.switch_to.frame(iframe)

    def select_menu(self, parent_menu_text, child_menu_text):
        """Hover on parent menu and click child submenu"""
        parent_menu = self.wait.until(
            EC.presence_of_element_located((By.XPATH, f"//div[text()='{parent_menu_text}']"))
        )
        # Hover over parent
        self.actions.move_to_element(parent_menu).perform()

        # Click child submenu
        child_menu = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{child_menu_text}']"))
        )
        child_menu.click()