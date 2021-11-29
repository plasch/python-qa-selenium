from selenium.webdriver import ActionChains


def test_drag_and_drop(browser):

    browser.get("https://konflic.github.io/front_example/pages/draganddrop.html")
    browser.maximize_window()

    actions = ActionChains(browser)

    # Итерируемся по 10 элементам которые нужно перебросить
    for i in range(1, 11):
        # Создаю строки для селекторов
        card_id = "card{}".format(i)
        zone_id = "zone{}".format(i)
        # Нахожу нужные элементы
        card_element = browser.find_element_by_id(card_id)
        zone_element = browser.find_element_by_id(zone_id)
        # Создаю действие
        actions.click_and_hold(card_element).pause(0.5).move_to_element(zone_element).pause(0.5).release()

    actions.perform()
