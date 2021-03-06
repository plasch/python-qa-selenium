from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def wait_title(title, driver, timeout=3):
    try:
        WebDriverWait(driver, timeout).until(EC.title_is(title))
    except TimeoutException:
        # Выбрасываю своё исключение и добавляю сообщение
        raise AssertionError("Ждал что title будет: '{}' но он был '{}'".format(title, driver.title))


def assert_element(selector, driver, timeout=2):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    except TimeoutException:
        # Перехватываем исключение и атачим скриншот
        driver.save_screenshot("{}.png".format(driver.session_id))
        # Выбрасываем AssertionError
        raise AssertionError("Не дождался видимости элемента: {}".format(selector))
