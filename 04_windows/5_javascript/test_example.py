import time

import pytest
from config import CHROMEDRIVER
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_extension("ublock.crx")
    wd = webdriver.Chrome(executable_path=CHROMEDRIVER, options=options)
    wd.get("https://konflic.github.io/front_example/")
    return wd


def test_disabled_button(browser):
    browser.get("https://konflic.github.io/front_example")
    browser.maximize_window()

    # Сначала проверяем клик по задизейбленой кнопке
    dis_btn = browser.find_element_by_id("disabled")
    dis_btn.click()
    time.sleep(1)  # Для демонстрации

    # Проверяем что не видна модалка
    WebDriverWait(browser, 3).until_not(EC.visibility_of(browser.find_element_by_id("myModal")))

    #  Убираем атрибут через js и проверяем
    js_code = "$('#disabled')[0].disabled = false;"
    browser.execute_script(js_code)

    # Поиск элементов на странице
    web_el = browser.execute_script("return $('#disabled')[0]")

    time.sleep(1)  # Для демонстрации
    dis_btn.click()
    time.sleep(1)  # Для демонстрации

    # Проверяем что видна модалка
    WebDriverWait(browser, 3).until(EC.visibility_of(browser.find_element_by_id("myModal")))

    with open("upload.js") as f:
        browser.execute_script(f.read())

    time.sleep(5)
