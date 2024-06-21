from bs4 import BeautifulSoup
import requests
from selenium import webdriver

url = ""

responce = requests.get(url)
soup = BeautifulSoup(responce.text, 'html.parser')
