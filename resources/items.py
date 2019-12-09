import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required
import bs4 as bs 
import urllib.request
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#import data stored to variables from scraping scripts and use that to create item. use payload['url'] to scrape the page and use the scraped data to create an item here instead of in on initialize in models.py
items = Blueprint('items', 'items')

#create route for items
@items.route('/<listId>', methods=['POST'])
@login_required
def create_item(listId):
	payload = request.get_json()
	#query for List to add item to
	found_list = models.List.get_by_id(listId)

	if(payload['url'].find('farfetch') != -1):
		print('url contains farfetch')
		farfetch_url = (payload['url'])

		sauce = urllib.request.urlopen(farfetch_url).read()

		#Load the plain html data into a variable
		soup = bs.BeautifulSoup(sauce, 'html.parser')

		#this gets the original price for and if applicable discounted price of an item on farfetch
		orig_price = soup.find('span', {'class': '_ffbca2 _1fe24a'})
		farfetch_orig_price_text = orig_price.get_text().strip()


		#discounted price 
		disc_price = soup.select('#slice-pdp > div > div._c84e0a > div._715521 > div._844eda > div > strong')
		farfetch_disc_price_text = disc_price[0].get_text().strip()

		#this will get the name of the item
		name = soup.find('span', {'class': '_b4693b'})
		farfetch_name_text = name.get_text().strip()


		#this will get the image src for item
		image = soup.find('img', {'class': '_221e30'})
		farfetch_image_src = image['src']

		item_object_farfetch = models.Item(url = farfetch_url, name = farfetch_name_text, image =farfetch_image_src, original_price = farfetch_orig_price_text, disc_price = farfetch_disc_price_text, notif_preference = '25')
		#turn into dict before creating record in db
		item_dict_farfetch = model_to_dict(item_object_farfetch)
		#create the new item with payload info
		farfetch_item = models.Item.create(
			**item_dict_farfetch
		)

		#turn to dict before sending response
		item_dict = model_to_dict(farfetch_item)
		print(item_dict)
	elif(payload['url'].find('target') != -1):
		print('url contains target')
		driver = webdriver.Chrome(executable_path='/Users/griffindelgado/Downloads/chromedriver')

		#this is the url that will be parsed
		target_url = (payload['url'])

		#5 second delay to load page and scrape before returning error 
		delay = 5

		#this makes a simple get request to the url
		driver.get(target_url)

		#this block will get us the original price 
		try:
			#tell the webDriver to wait to scrape until the element is located by it's css selector. If the element has not been rendered and found it won't begin the scrape
			element_orig_price= WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#viewport > div:nth-child(4) > div > div.Row-uds8za-0.gnKDVb > div.Col-favj32-0.h-padding-h-default.h-padding-t-tight.styles__StyledCol-sc-1n8m629-12.eiisQZ > div.h-padding-b-default > div.h-text-red > div:nth-child(3) > span')))
			print('element is ready!')
			#turn all element data into text
			target_orig_price_text = element_orig_price.text
			print(target_orig_price_text)
			#execute script once element is rendered
			html_of_interest = driver.execute_script('return arguments[0].innerHTML',element_orig_price,)
			sel_soup=BeautifulSoup(html_of_interest, 'html.parser')
		except:#if error present 
			print('error scraping resource')

		#second try except to get discounted price 
		try:
			element_disc_price= WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#viewport > div:nth-child(4) > div > div.Row-uds8za-0.gnKDVb > div.Col-favj32-0.h-padding-h-default.h-padding-t-tight.styles__StyledCol-sc-1n8m629-12.eiisQZ > div.h-padding-b-default > div.h-text-red > div.h-text-bold.style__PriceFontSize-gob4i1-0.eLdTvF')))
			print('element is ready!')
			target_disc_price_text = element_disc_price.text
			print(target_disc_price_text)
			html_of_interest = driver.execute_script('return arguments[0].innerHTML',element_disc_price,)
			sel_soup=BeautifulSoup(html_of_interest, 'html.parser')
		except:
			print('error scraping resource')



		#url to be scraped / will later change to a variable that will hold url user inputs
		sauce = urllib.request.urlopen(target_url).read()

		#load all html in variable
		soup = bs.BeautifulSoup(sauce, 'html.parser')


		#scrapes item name 
		target_name = soup.find('h1', {'class': 'h-margin-b-none h-margin-b-tiny h-text-bold Heading__StyledHeading-sc-6yiixr-0 jHwOVX'})
		target_name_text = target_name.get_text().strip()
		print(target_name_text)

		#scraps image for item
		target_image = soup.find('img')
		target_image_src = target_image['src']
		print(target_image_src)

		item_object_target = models.Item(url = target_url, name = target_name_text, image =target_image_src, original_price = target_orig_price_text, disc_price = target_disc_price_text, notif_preference = '25')
		#turn into dict before creating record in db
		item_dict_target = model_to_dict(item_object_target)
		#create the new item with payload info
		target_item = models.Item.create(
			**item_dict_target
		)

		#turn to dict before sending response
		item_dict = model_to_dict(target_item)
		print(item_dict)


	return jsonify(data=str(item_dict), status={'code': 201, 'message': "Successfully created item"}), 201

#get a lists items
@items.route('/<listId>', methods=['GET'])
@login_required
def get_lists_items(listId):
	try:
		#query for all items that belong to the postid being passed in the uurl
		items = [model_to_dict(items) for items in models.Item.select().where(models.Item.list_id == listId)]
		return jsonify(data=items, status={'code': 200, 'message': 'Successfully retreived all items'}), 200
	except models.DoesNotExist:
		return jsonify(data={}, status={'code': 401, 'message': 'Error retrieving resources'}), 401

#delete an item
@items.route('/<itemId>', methods=['DELETE'])
@login_required
def delete_item(itemId):
	#query for item that matches id
	item_to_delete = models.Item.get_by_id(itemId)
	print('\nthis is item_to_delete')
	print(item_to_delete)
	item_to_delete.delete_instance()
	return jsonify(data={}, status={'code': 200, 'message': 'Successfully delete item'})














