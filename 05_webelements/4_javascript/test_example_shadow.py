from selenium.webdriver.common.by import By


# Не работает в интерактивном режиме!
def test_disabled_button(browser):
    browser.get("https://konflic.github.io/front_example/pages/shadow.html")

    # Так не сработает
    # button = browser.find_element("css selector", "#button")
    # button.click()

    # Используем js
    def shadow_element(element, locator):
        return browser.execute_script('return arguments[0].shadowRoot.querySelector("{}")'.format(locator), element)

    btn = shadow_element(element=browser.find_element_by_css_selector("#elem"), locator="#button")
    btn.click()

    assert browser.find_element_by_css_selector("body > div").text == "SHADOW!"
