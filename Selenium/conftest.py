#create a fixture for Invoke chrome browser and close the chrome browser.

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope = "function")
def setup(request):
    service = Service(ChromeDriverManager().install())
    #driver instance is created to use web driver globally in the test script
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)

    #driver set locally is passed to request at class level so that drive is
    # available for other testcases in the tests folder
    request.cls.driver = driver
    yield
    driver.quit()










