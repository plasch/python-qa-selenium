import time

from locators import MainPage, CatalogPage
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


def test_select_value(browser):
    browser.get("https://demo.opencart.com/")
    desktops_link = browser.find_element(*MainPage.menu.desktops.link)

    time.sleep(2)
    ActionChains(browser).move_to_element(desktops_link).pause(2).perform()
    browser.find_element(*MainPage.menu.desktops.show_all).click()
    select_limit = Select(browser.find_element(*CatalogPage.select_limit))

    time.sleep(2)
    select_limit.select_by_visible_text("100")
    select_limit = Select(browser.find_element(*CatalogPage.select_limit))
    assert select_limit.first_selected_option.text == "100"

    time.sleep(2)
    select_limit.select_by_visible_text("50")
    select_limit = Select(browser.find_element(*CatalogPage.select_limit))
    assert select_limit.first_selected_option.text == "50"
