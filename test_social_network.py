from tokiopages import SocialNetwork
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tokiopages import Locators


def test_go_to_vk(driver):
    vk = SocialNetwork(driver)
    vk.get_to_site()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.GO_TO_VK))
    vk.go_to_vk()

    assert driver.current_url == 'https://vk.com/club10958821'
