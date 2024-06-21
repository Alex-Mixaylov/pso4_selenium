from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver import Keys #Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By #Библиотека с поиском элементов на сайте
import time

url1 = 'https://en.wikipedia.org/wiki/Document_Object_Model'
url2 = 'https://ru.wikipedia.org/wiki/Selenium'
url_wiki = 'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'

# responce = requests.get(url)
# soup = BeautifulSoup(responce.text, 'html.parser')

# browser = webdriver.Chrome()
# browser.get(url1)
# browser.save_screenshot("dom.png")
# time.sleep(10)
# browser.get(url2)
# browser.save_screenshot("selenium.png")
# time.sleep(10)
# browser.refresh()
# time.sleep(5)
# browser.quit(

browser = webdriver.Chrome()
browser.get(url_wiki)

assert "Википедия" in browser.title
time.sleep(5)
search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys("Тасманийский дьявол")
time.sleep(2)
search_box.send_keys(Keys.RETURN)
time.sleep(2)

a = browser.find_element(By.LINK_TEXT, "Лицевая опухоль тасманийского дьявола")
a.click()
time.sleep(10)