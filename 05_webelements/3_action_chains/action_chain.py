import random
import time

from config import CHROMEDRIVER
from selenium.webdriver import ActionChains
from selenium import webdriver

chrome = webdriver.Chrome(executable_path=CHROMEDRIVER)

# Долгое открытие страницы
chrome.implicitly_wait(20)
chrome.maximize_window()

# Открываем страницу и закрываем поп-ап
chrome.get("https://sketch.io/sketchpad/en/")
chrome.find_element_by_css_selector(".alertify-message .close-button").click()

# Получаем область в которой можно рисовать
draw_area = chrome.find_element_by_tag_name("sketch-docviewport")

# Создаем объект ActionChains в который будем записывать наши действия
actions = ActionChains(chrome)

# Наполняем actions 10 разными действиями
for i in range(20):
    # Определяем случайные координаты по x и y
    random_x = random.randint(300, 700)
    random_y = random.randint(300, 700)
    # Нажимаем на кнопку мыши в этих координатах и не отпускаем
    actions.move_to_element_with_offset(draw_area, random_x, random_y).click_and_hold()
    # Определяем случайные величины для смешения курсора от текущей точки
    offset_x = random.randint(-150, 250)
    offset_y = random.randint(-200, 250)
    # Выполняем движение мышью на заданное количество пикселей и отпускаем
    actions.move_by_offset(offset_x, offset_y)

# Выполняем все накопленные в цикле for действия начиная с первого
actions.release().perform()
