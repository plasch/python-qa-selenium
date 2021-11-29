from selenium.webdriver.common.by import By

from config import CHROMEDRIVER
from selenium import webdriver

chrome = webdriver.Chrome(executable_path=CHROMEDRIVER)

chrome.get("https://yandex.ru")

# search_input это объект типа WebElement
search_input = chrome.find_element(By.CSS_SELECTOR, "input#text")

print(type(search_input))

chrome.close()
