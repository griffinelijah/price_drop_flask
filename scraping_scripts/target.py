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
target_url = ('https://www.target.com/p/lg-55-39-39-class-4k-uhd-smart-oled-tv-oled55b9pua/-/A-52328755')

#5 second delay to load page and scrape before returning error 
delay = 5

#this makes a simple get request to the url
driver.get(target_url)

try:
	element_disc_price= WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.h-padding-b-default > div.h-text-red > div:nth-child(3)')))
	print('element is ready!')
	element__disc_text = element_disc_price.text
	print(element__disc_text)
	html_of_interest = driver.execute_script('return arguments[0].innerHTML',element,)
	sel_soup=BeautifulSoup(html_of_interest, 'html.parser')
except:
	print('error scraping resource')

#second try except to get discounted price 
try:
	element_orig_price= WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#viewport > div:nth-child(4) > div > div.Row-uds8za-0.gnKDVb > div.Col-favj32-0.h-padding-h-default.h-padding-t-tight.styles__StyledCol-sc-1n8m629-12.eiisQZ > div.h-padding-b-default > div.h-text-red > div.h-text-bold.style__PriceFontSize-gob4i1-0.eLdTvF')))
	print('element is ready!')
	element_orig_text = element_orig_price.text
	print(element_orig_text)
	html_of_interest = driver.execute_script('return arguments[0].innerHTML',element_orig_price,)
	sel_soup=BeautifulSoup(html_of_interest, 'html.parser')
except:
	print('error scraping resource')



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
