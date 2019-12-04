from bs4 import BeautifulSoup
import bs4 as bs
import urllib.request
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/Users/griffindelgado/Downloads/chromedriver')

target_url = ('https://www.target.com/p/vizio-d-series-40-class-39-50-diag-1080p-full-array-led-smart-hdtv-d40f-g9/-/A-53855744')

delay = 5

driver.get(target_url)

element= WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.h-padding-b-default > div.h-text-red > div:nth-child(3)')))
print('element is ready!')
element_text = element.text
print(element_text)
html_of_interest = driver.execute_script('return arguments[0].innerHTML',element)
sel_soup=BeautifulSoup(html_of_interest, 'html.parser')




    # viewport > div:nth-child(4) > div > div.Row-uds8za-0.gnKDVb > div.Col-favj32-0.h-padding-h-default.h-padding-t-tight.styles__StyledCol-sc-1n8m629-12.eiisQZ > div.h-padding-b-default > div.h-text-red > div:nth-child(3)

#url to be scraped / will later change to a variable that will hold url user inputs
sauce = urllib.request.urlopen(target_url).read()

#load all html in variable
soup = bs.BeautifulSoup(sauce, 'html.parser')

#scrapes price


#scrapes item name 
name = soup.find('h1', {'class': 'h-margin-b-none h-margin-b-tiny h-text-bold Heading__StyledHeading-sc-6yiixr-0 jHwOVX'})
name_text = name.get_text()
print(name_text)

#scraps image for item
image = soup.find('img')
image_src = image['src']
print(image_src)
