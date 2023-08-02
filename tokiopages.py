from baseapp import BasePage
from selenium.webdriver.common.by import By


class Locators:
    SEARCH_FIELD = (By.XPATH, '//*[@id="search"]/input[2]')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="search"]/input[3]')

    MENU_BUTTON = (By.XPATH, '//*[@id="wrapper__col"]/header/div[1]/nav/ul/li[2]/a')
    DELIVERY_BUTTON = (By.XPATH, '//*[@id="wrapper__col"]/header/div[1]/nav/ul/li[3]/a')
    PROMO_BUTTON = (By.XPATH, '//*[@id="wrapper__col"]/header/div[1]/nav/ul/li[4]/a')
    NEWS_BUTTON = (By.XPATH, '//*[@id="wrapper__col"]/header/div[1]/nav/ul/li[5]/a')
    ADDRESSES_BUTTON = (By.XPATH, '//*[@id="wrapper__col"]/header/div[1]/nav/ul/li[6]/a')

    SELECT_CITY = (By.XPATH, '//*[@id="mCSB_1_container"]/div[2]/a')
    POPUP_CITY_LIST = (By.XPATH, '//*[@id="callback_form_div"]/ul/li[2]/a')

    GO_TO_VK = (By.XPATH, '//*[@id="mCSB_1_container"]/div[6]/a[1]')


class Search(BasePage):
    def enter_the_word(self, word):
        search_filed = self.find_element(Locators.SEARCH_FIELD)
        search_filed.click()
        search_filed.send_keys(word)
        return search_filed

    def click_on_the_search_button(self):
        return self.find_element(Locators.SEARCH_BUTTON, time=2).click()


class NavigationMenu(BasePage):
    def menu_button(self):
        menu = self.find_element(Locators.MENU_BUTTON)
        menu.click()
        return menu

    def delivery_button(self):
        delivery = self.find_element(Locators.DELIVERY_BUTTON)
        delivery.click()
        return delivery

    def promo_button(self):
        promo = self.find_element(Locators.PROMO_BUTTON)
        promo.click()
        return promo

    def news_button(self):
        news = self.find_element(Locators.NEWS_BUTTON)
        news.click()
        return news

    def addresses_button(self):
        address = self.find_element(Locators.ADDRESSES_BUTTON)
        address.click()
        return address


class SelectCity(BasePage):
    def select_city(self):
        city = self.find_element(Locators.SELECT_CITY)
        city.click()
        return city

    def popup_city_list(self):
        city_list = self.find_element(Locators.POPUP_CITY_LIST)
        city_list.click()
        return city_list


class SocialNetwork(BasePage):
    def go_to_vk(self):
        vk = self.find_element(Locators.GO_TO_VK)
        vk.click()
        return vk
