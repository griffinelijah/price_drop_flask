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
newegg_url = ('https://www.newegg.com/msi-geforce-rtx-2070-super-rtx-2070-super-ventus-oc/p/N82E16814137438?Item=N82E16814137438&cm_sp=Homepage_BS-_-P2_14-137-438-_-12042019')

#5 second delay to load page and scrape before returning error 
delay = 5

#this makes a simple get request to the url
driver.get(newegg_url)

try:	
	element= WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#landingpage-price > div > div > ul > li.price-current')))
	print('element is ready!')
	price_text = element.text
	print(price_text)
	html_of_interest = driver.execute_script('return arguments[0].innerHTML',element)
	sel_soup=BeautifulSoup(html_of_interest, 'html.parser')
except:
	print('error scraping resource')