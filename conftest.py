import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session')
def driver():
    driver_service = Service(ChromeDriverManager(url='https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json', driver_version='115.0.5790.110').install())
    driver = webdriver.Chrome(service=driver_service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
