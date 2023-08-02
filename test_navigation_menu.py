from tokiopages import NavigationMenu
from selenium.webdriver.common.by import By
from selenium import webdriver


def test_menu_button(driver):
    menu_page = NavigationMenu(driver)
    menu_page.get_to_site()
    menu_page.menu_button()

    assert driver.current_url == 'https://www.tokyo-city.ru/menu.html'
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'МЕНЮ СЛУЖБЫ ДОСТАВКИ ТОКИО-CITY'


def test_delivery_button(driver):
    delivery_page = NavigationMenu(driver)
    delivery_page.get_to_site()
    delivery_page.delivery_button()

    assert driver.current_url == 'https://www.tokyo-city.ru/delivery.html'
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'УСЛОВИЯ ДОСТАВКИ ПО САНКТ-ПЕТЕРБУРГУ И ОБЛАСТИ'


def test_promo_button(driver):
    promo_page = NavigationMenu(driver)
    promo_page.get_to_site()
    promo_page.promo_button()

    assert driver.current_url == 'https://www.tokyo-city.ru/action.html'
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'В РЕСТОРАНАХ И СЛУЖБЕ ДОСТАВКИ ' \
                                                          '«ТОКИО-CITY» ДЕЙСТВУЮТ СЛЕДУЮЩИЕ АКЦИИ'


def test_news_button(driver):
    news_page = NavigationMenu(driver)
    news_page.get_to_site()
    news_page.news_button()

    assert driver.current_url == 'https://www.tokyo-city.ru/news.html'
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'НОВОСТИ'


def test_addresses_button(driver):
    address_page = NavigationMenu(driver)
    address_page.get_to_site()
    address_page.addresses_button()

    assert driver.current_url == 'https://www.tokyo-city.ru/adresses.html'
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'АДРЕСА РЕСТОРАНОВ ТОКИО-CITY'
