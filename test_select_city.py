from tokiopages import SelectCity

def test_select_city(driver):
    select_city = SelectCity(driver)
    select_city.get_to_site()
    select_city.select_city()
    select_city.popup_city_list()

    assert driver.current_url == 'https://msk.tokyo-city.ru/'