import os
import time

import pytest
from config import CHROMEDRIVER
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
    driver.implicitly_wait(10)

    def fin(): driver.quit()

    request.addfinalizer(fin)
    return driver


def test_upload_radical(driver):
    driver.get('https://radikal.ru')
    uploader = driver.find_element(By.CSS_SELECTOR, ".upload1")
    filename = os.path.join(os.path.dirname(__file__), 'selenium.png')
    uploader.send_keys(filename)
    time.sleep(10)
