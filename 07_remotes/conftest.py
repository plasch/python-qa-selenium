import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

DRIVERS_FOLDER = os.path.expanduser("~/Dev/drivers")
CHROMEDRIVER = f"{DRIVERS_FOLDER}/chromedriver"
GECKODRIVER = f"{DRIVERS_FOLDER}/geckodriver"
OPERADRIVER = f"{DRIVERS_FOLDER}/operadriver"


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        choices=["chrome", "firefox", "opera", "MicrosoftEdge"]
    )
    parser.addoption("--executor", default="192.168.1.88")
    parser.addoption("--platform", default="linux")


@pytest.fixture
def firefox(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def chrome(request):
    options = webdriver.ChromeOptions()
    options.headless = False
    service = Service(os.path.expanduser(CHROMEDRIVER))
    wd = webdriver.Chrome(service=service, options=options)
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def remote(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    platform = request.config.getoption("--platform")

    driver = webdriver.Remote(
        command_executor=f"http://{executor}:4444/wd/hub",
        desired_capabilities={"browserName": browser, "platformName": platform}
    )
    driver.implicitly_wait(2)
    driver.maximize_window()

    request.addfinalizer(driver.quit)

    return driver
