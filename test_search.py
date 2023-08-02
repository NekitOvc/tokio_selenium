from tokiopages import Search
from urllib.parse import unquote

def test_search(driver):
    main_page = Search(driver)
    main_page.get_to_site()
    word = 'филадельфия'
    main_page.enter_the_word(word)
    main_page.click_on_the_search_button()

    url = unquote(driver.current_url)

    assert url == f'https://www.tokyo-city.ru/spisok-product-search.html?p_f_2_temp_id=116&p_f_2_title={word}'