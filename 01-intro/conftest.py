import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="Browser to run tests",
        choices=["chrome", "firefox", "safari", "edge", "opera"]
    )
    parser.addoption(
        "--dfolder", default=os.path.expanduser("~/Dev/drivers"), help="Root folder for drivers"
    )
    parser.addoption(
        "--ext", default="", help="If you use windows pass .exe"
    )
    parser.addoption(
        "--headless", action="store_true", help="To run browser headless"
    )


@pytest.fixture
def browser(request):
    driver = None
    _dfolder = request.config.getoption("--dfolder")
    _browser = request.config.getoption("--browser")
    _headless = request.config.getoption("--headless")
    _ext = request.config.getoption("--ext")

    if _browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = _headless
        driver = webdriver.Chrome(executable_path=f"{_dfolder}/chromedriver{_ext}", options=options)
    elif _browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = _headless
        # DeprecationWarning: executable_path has been deprecated, please pass in a Service object
        service = Service(os.path.expanduser(f"{_dfolder}/geckodriver{_ext}"))
        driver = webdriver.Firefox(service=service, options=options)
    elif _browser == "safari":
        driver = webdriver.Safari()
    elif _browser == "edge":
        driver = webdriver.Edge(executable_path=f"{_dfolder}/msedgedriver{_ext}")

    def final():
        driver.quit()

    request.addfinalizer(final)

    return driver
