
from sre_parse import WHITESPACE
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

url = 'https://tabs.ultimate-guitar.com/tab/nirvana/smells-like-teen-spirit-tabs-202727'


options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')
links = soup.findAll("span",class_= "_3rlxz")

with open('output.txt', 'w') as f:
    for i in links:
        print(i.text)
        f.write(i.text)
        f.write("\n")




