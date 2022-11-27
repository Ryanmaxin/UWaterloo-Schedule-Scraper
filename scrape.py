import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

PATH = "H:\webdrivers\chromedriver.exe"

web = webdriver.Chrome(executable_path=PATH)
# url = "https://classes.uwaterloo.ca/under.html"
url2 = "https://www.google.com/"

web.get(url2)
time.sleep(2)
# term = 1231
# subject = "SPCOM"
# course_number = 225

# term_select = web.find_element('xpath','//*[@id="term"]')
# term_select.send_keys(term)
