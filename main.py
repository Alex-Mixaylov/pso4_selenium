from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

url1 = 'https://en.wikipedia.org/wiki/Document_Object_Model'
url2 = 'https://ru.wikipedia.org/wiki/Selenium'

# responce = requests.get(url)
# soup = BeautifulSoup(responce.text, 'html.parser')

browser = webdriver.Chrome()
browser.get(url1)
browser.save_screenshot("dom.png")
time.sleep(10)
browser.get(url2)
browser.save_screenshot("selenium.png")
time.sleep(10)
browser.quit()