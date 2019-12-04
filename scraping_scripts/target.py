from bs4 import BeautifulSoup
import bs4 as bs
import urllib.request
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/Users/griffindelgado/Downloads/chromedriver')

target_url = ('https://www.target.com/p/lg-55-39-39-class-4k-uhd-smart-oled-tv-oled55b9pua/-/A-52328755')

delay = 5

driver.get(target_url)

element= WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.h-padding-b-default > div.h-text-red > div:nth-child(3)')))
print('element is ready!')
element_text = element.text
print(element_text)
html_of_interest = driver.execute_script('return arguments[0].innerHTML',element)
sel_soup=BeautifulSoup(html_of_interest, 'html.parser')

#url to be scraped / will later change to a variable that will hold url user inputs
sauce = urllib.request.urlopen(target_url).read()

#load all html in variable
soup = bs.BeautifulSoup(sauce, 'html.parser')


#scrapes item name 
name = soup.find('h1', {'class': 'h-margin-b-none h-margin-b-tiny h-text-bold Heading__StyledHeading-sc-6yiixr-0 jHwOVX'})
name_text = name.get_text()
print(name_text)

#scraps image for item
image = soup.find('img')
image_src = image['src']
print(image_src)
