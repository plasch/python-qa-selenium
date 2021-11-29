import time
import os

from config import CHROMEDRIVER
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome(executable_path=CHROMEDRIVER)

chrome.get("https://konflic.github.io/front_example/editor/index.html")

input_field = chrome.find_element(value="editor_text")

input_field.send_keys("Левый марш.")

input_field.send_keys(Keys.ENTER)

input_field.send_keys("""
Разворачивайтесь в марше!
Словесной не место кляузе.
Тише, ораторы!
Ваше
    слово,
        товарищ маузер.
""")

input_field.send_keys(Keys.ENTER)

author = "А. С. Пушкин."

input_field.send_keys(author)

for _ in range(len(author)):
    time.sleep(0.1)
    input_field.send_keys(Keys.BACK_SPACE)

input_field.send_keys("В. В. Маяковский.")

input_field.send_keys(Keys.ENTER)

upload_field = chrome.find_element(value="file-uploader")

# Передача АБСОЛЮТНОГО пути в системе до файла
upload_field.send_keys(os.path.abspath("picture.png"))
