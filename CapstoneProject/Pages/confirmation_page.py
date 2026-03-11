import os
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.Logger import get_logger

logger = get_logger()


class ConfirmationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def verify_success_message(self):

        try:
            message = self.get_text((By.XPATH, "//legend[@id='confirmation-message']"))
            logger.info("Order placed successfully")

            return message

        except Exception as e:
            logger.error(f"Failed to verify confirmation message: {e}")
            raise

    def download_receipt(self):

        try:
            self.click((By.XPATH, "//a[@id='downloadpdf']"))
            logger.info("Receipt download started")

            time.sleep(5)

        except Exception as e:
            logger.error(f"Receipt download failed: {e}")
            raise

    def verify_download(self):

        try:
            download_path = os.path.join(os.path.expanduser("~"), "Downloads")
            file_path = os.path.join(download_path, "confirmation.pdf")

            timeout = 10
            start_time = time.time()

            while time.time() - start_time < timeout:
                if os.path.exists(file_path):
                    logger.info("Receipt downloaded successfully")
                    return True

                time.sleep(1)

            logger.error("Receipt not downloaded")
            return False

        except Exception as e:
            logger.error(f"Download verification failed: {e}")
            raise