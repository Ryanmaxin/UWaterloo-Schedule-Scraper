import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from dotenv import load_dotenv
import os
from sms import send_sms_via_email

while (True):
  try:
    PATH = r'C:\webdrivers\chromedriver.exe'

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service,service_args=["--verbose", "--log-path=D:\\qc1.log"],options=options)
    url = 'https://classes.uwaterloo.ca/under.html'

    driver.get(url)
    time.sleep(2)

    term = 1231
    subject = "SPCOM"
    course_number = 225

    term_select = driver.find_element('xpath','//*[@id="term"]')
    term_select.send_keys(term)

    subject_select = driver.find_element('xpath','//*[@id="ssubject"]')
    subject_select.send_keys(subject)

    course_number_select = driver.find_element('xpath','//*[@id="icournum"]')
    course_number_select.send_keys(course_number)

    submit = driver.find_element('xpath','/html/body/main/form/p[3]/input[1]')
    submit.click()

    table = driver.find_element('xpath','/html/body/main/p[2]/table')
    html_table = table.get_attribute('outerHTML')

    driver.quit()

    df = pd.read_html(html_table,flavor="bs4",header=3)
    data = df[0]
    data.drop(axis=0,labels=9,inplace=True)

    space_open = False
    enroll_cap = data['Enrl Cap']
    enroll_total = data['Enrl Tot']

    math_reserves_rows = [1,2,4,6,8]

    load_dotenv()
    number = os.environ.get('PHONENUM')
    email = os.environ.get('EMAIL')
    password = os.environ.get('PASSWORD')

    sender_credentials = (email,password)

    for row in math_reserves_rows:
      if enroll_total[row] < enroll_cap[row]:
        message = f"{int(enroll_cap[row]-enroll_total[row])} spaces opened up in {subject} {course_number}"
        send_sms_via_email(number,message,sender_credentials)
  except:
    print("problem with the script or manual exit")
  print("Ended Check. Checking again in 30 minutes")
  time.sleep(30*60)
  print("30 minutes is elapsed")
