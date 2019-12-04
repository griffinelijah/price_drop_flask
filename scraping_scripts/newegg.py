from bs4 import BeautifulSoup
import bs4 as bs
import urllib.request
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#this is the path to where the chrome driver.exe file is
driver = webdriver.Chrome(executable_path='/Users/griffindelgado/Downloads/chromedriver')

#this is the url that will be parsed
newegg_url = ('https://www.target.com/p/lg-55-39-39-class-4k-uhd-smart-oled-tv-oled55b9pua/-/A-52328755')

#5 second delay to load page and scrape before returning error 
delay = 5

#this makes a simple get request to the url
driver.get(newegg_url)


element= WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.h-padding-b-default > div.h-text-red > div:nth-child(3)')))
print('element is ready!')
element_text = element.text
print(element_text)
html_of_interest = driver.execute_script('return arguments[0].innerHTML',element)
sel_soup=BeautifulSoup(html_of_interest, 'html.parser')