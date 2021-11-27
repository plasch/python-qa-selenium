import time

from config import GECKODRIVER, CHROMEDRIVER
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(executable_path=CHROMEDRIVER)
chrome.maximize_window()
chrome.get("https://konflic.github.io/front_example/pages/iframes.html")

# Получаем iframe элементы на странице
frames = chrome.find_elements(By.CSS_SELECTOR, "iframe")

# Переключаемся в первый iframe в списке
chrome.switch_to.frame(frames[0])
chrome.find_element(By.NAME, "search").send_keys("MacBook")
chrome.find_element(By.XPATH, "//*[@id='search']//button[@type='button']").click()
# Возвращаемся в исходный контекст
chrome.switch_to.default_content()
chrome.find_element(By.ID, "main").click()
chrome.switch_to.alert.accept()
time.sleep(2)

# Переключаемся в iframe по имени
chrome.switch_to.frame("selenium")
chrome.find_element(By.CSS_SELECTOR, "button.navbar-toggler").click()
# Возвращаемся в исходный контекст
chrome.switch_to.default_content()
chrome.find_element(By.ID, "main").click()
chrome.switch_to.alert.accept()
time.sleep(2)

# Переключаемся по порядковому индексу
chrome.switch_to.frame(frames[2])
chrome.find_element(By.ID, "state").send_keys("SomeTextForInput")
chrome.find_element(By.CSS_SELECTOR, "#submit").click()
# Возвращаемся в исходный контекст
chrome.switch_to.default_content()
chrome.find_element(By.ID, "main").click()
chrome.switch_to.alert.accept()
time.sleep(2)

chrome.close()
