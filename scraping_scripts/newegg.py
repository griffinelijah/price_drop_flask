# from bs4 import BeautifulSoup
# import bs4 as bs
# import urllib.request
# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# #this is the path to where the chrome driver.exe file is
# driver = webdriver.Chrome(executable_path='/Users/griffindelgado/Downloads/chromedriver')

# #this is the url that will be parsed
# newegg_url = ('https://www.newegg.com/zotac-geforce-gtx-1060-zt-p10620a-10m/p/N82E16814500454?Item=N82E16814500454')

# #5 second delay to load page and scrape before returning error 
# delay = 5

# #this makes a simple get request to the url
# driver.get(newegg_url)

# #this scrapes the original price if not discounted from newegg
# try:	
# 	#using selenium we wait for the web page to load so we can scrape the dynamic elements.
# 	#once the web page loads we begin our scrape by finding the li the price lives in by the css selector
# 	element= WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#landingpage-price > div > div > ul > li.price-current')))
# 	print('element is ready!')
# 	not_disc_price_text = element.text
# 	print(not_disc_price_text)
# 	#this executes the script and returns the scraped element
# 	html_of_interest = driver.execute_script('return arguments[0].innerHTML',element)
# 	sel_soup=BeautifulSoup(html_of_interest, 'html.parser')
# except:
# 	print('error scraping resource')

# #this scrapes the originial price from IF the item is discounted newegg
# try:	
# 	element= WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#landingpage-price > div > div:nth-child(2) > ul > li.price-was')))
# 	print('element is ready!')
# 	orig_price_if_disc_text = element.text
# 	print(orig_price_if_disc_text)
# 	#this executes the script and returns the scraped element
# 	html_of_interest = driver.execute_script('return arguments[0].innerHTML',element)
# 	sel_soup=BeautifulSoup(html_of_interest, 'html.parser')
# except:
# 	print('error scraping resource')

# #this will get the discounted price if the item is discounted
# try:	
# 	element= WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#landingpage-price > div > div:nth-child(2) > ul > li.price-current > strong')))
# 	print('element is ready!')
# 	orig_price_if_disc_text = element.text
# 	print(orig_price_if_disc_text)
# 	#this executes the script and returns the scraped element
# 	html_of_interest = driver.execute_script('return arguments[0].innerHTML',element)
# 	sel_soup=BeautifulSoup(html_of_interest, 'html.parser')
# except:
# 	print('error scraping resource')

# # https://c1.neweggimages.com/ProductImage/14-932-212-V03.jpg?ex=2
# # we will scrape the image with this as it is dynamically loaded as well
# # not properly scraping image always come back blank. Can't use most of neweggs image srcs as they are not URL's
# try:	
# 	image= WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#A2')))
# 	print('image is ready!')
# 	# image_text = element2.text
# 	print(image.get_text())
# 	html_of_interest = driver.execute_script('return arguments[0].innerHTML', image)
# 	sel_soup=BeautifulSoup(html_of_interest, 'html.parser')
# except:
# 	print('error scraping resource')



# #url to be scraped / will later change to a variable that will hold url user inputs
# sauce = urllib.request.urlopen(newegg_url).read()

# #load all html in variable
# soup = bs.BeautifulSoup(sauce, 'html.parser')


# name = soup.find('h1', {'id': 'grpDescrip_h'})
# name_text = name.get_text().strip()
# print(name_text)















