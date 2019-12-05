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
newegg_url = ('https://www.newegg.com/gigabyte-geforce-rtx-2070-super-gv-n207sgaming-oc-8gd/p/N82E16814932212')

#5 second delay to load page and scrape before returning error 
delay = 5

#this makes a simple get request to the url
driver.get(newegg_url)

#this scrapes the price from newegg
try:	
	#using selenium we wait for the web page to load so we can scrape the dynamic elements.
	#once the web page loads we begin our scrape by finding the li the price lives in by the css selector
	element= WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#landingpage-price > div > div > ul > li.price-current')))
	print('element is ready!')
	price_text = element.text
	print(price_text)
	#this executes the script and returns the scraped element
	html_of_interest = driver.execute_script('return arguments[0].innerHTML',element)
	sel_soup=BeautifulSoup(html_of_interest, 'html.parser')
except:
	print('error scraping resource')

#we will scrape the image with this as it is dynamically loaded as well
#not properly scraping image always come back blank. Can't use most of neweggs image srcs as they are not URL's
# try:	
# 	element2= WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainSlide_014-932-212')))
# 	print('element2 is ready!')
# 	image_text = element2.text
# 	print(image_text)
	
# 	html_of_interest2 = driver.execute_script('return arguments[0].innerHTML',element2)
# 	sel_soup=BeautifulSoup(html_of_interest2, 'html.parser')
# except:
# 	print('error scraping resource')



#url to be scraped / will later change to a variable that will hold url user inputs
sauce = urllib.request.urlopen(newegg_url).read()

#load all html in variable
soup = bs.BeautifulSoup(sauce, 'html.parser')


name = soup.find('h1', {'id': 'grpDescrip_h'})
name_text = name.get_text().strip()
print(name_text)















