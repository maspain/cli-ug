from dataclasses import dataclass
from os import link
from sre_parse import WHITESPACE
import curses
from curses import A_BLINK, wrapper
from tkinter import Entry
from tkinter.tix import Tree
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions

url = 'https://tabs.ultimate-guitar.com/tab/nirvana/smells-like-teen-spirit-tabs-202727'

search_url = "https://www.ultimate-guitar.com/search.php?search_type=title&value=wish%20you%20were%20here"

@dataclass
class TableEntry:
    link: str
    rating: int

    

'3b534a19-8529-4285-a558-3bfa9c36552d'


def get_top_tabs(driver, options):
    driver.get(search_url)
    ##links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Wish")
    soup = BeautifulSoup(driver.page_source, 'lxml')

    ratings = soup.find_all('div', class_='_3qD3P')

    ## attempt to pull rating data, seems slow (but it is Python sooo)
    children = ratings[0].find_all("span")

    tabs = soup.find_all('a', class_='_3DU-x JoRLr _3dYeW', href=True)

    
    print_table(tabs, ratings)


def print_table(entries, ratings):
    index = 0
    
    for i in entries:
        print(index,": ",i.text, end='\n')
        index += 1


def get_song_tabs(driver, url):
    driver.get(search_url)
    soup = BeautifulSoup(driver.page_source, 'lxml') 
    links = soup.findAll("span",class_= "_3rlxz")

    with open('output.txt', 'w') as f:
        for i in links:
            print(i.text)
            f.write(i.text)
            f.write("\n")

def main():

    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)

    while True:

        c = input()

        if c == ord('q'):
            driver.quit()
            break
        elif c == ord('s'):
            get_song_tabs(driver, url)
        elif c == 't':
            links = get_top_tabs(driver, options)

    





if __name__ == "__main__":
    main()





