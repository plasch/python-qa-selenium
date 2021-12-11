

def test_first_test(browser):
    browser.get("https://yandex.ru")
    print(browser.title)
    assert "Яндекс" in browser.title
    browser.refresh()
    assert "Яндекс" in browser.title
