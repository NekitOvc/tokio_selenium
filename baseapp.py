from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.tokyo-city.ru/'

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))

    def get_to_site(self):
        return self.driver.get(self.base_url)
