from framework import wait_title
from framework import assert_element


def test_check_exception(browser):
    browser.get("https://konflic.github.io/front_example/")
    wait_title("Example Project", browser)
    assert_element("#myBtn", browser)
