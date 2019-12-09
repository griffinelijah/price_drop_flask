import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required
import bs4 as bs 
import urllib.request

#import data stored to variables from scraping scripts and use that to create item. use payload['url'] to scrape the page and use the scraped data to create an item here instead of in on initialize in models.py
items = Blueprint('items', 'items')

#create route for items
@items.route('/<listId>', methods=['POST'])
@login_required
def create_item(listId):
	payload = request.get_json()
	#query for List to add item to
	found_list = models.List.get_by_id(listId)

	farfetch_url = (payload['url'])

	sauce = urllib.request.urlopen(farfetch_url).read()

	#Load the plain html data into a variable
	soup = bs.BeautifulSoup(sauce, 'html.parser')

	#this gets the original price for and if applicable discounted price of an item on farfetch
	# orig_price = soup.select('#slice-pdp > div > div._c84e0a > div._715521 > div._844eda > div > span._ffbca2._1fe24a')
	orig_price = soup.find('span', {'class': '_ffbca2 _1fe24a'})
	print('\nthis is the originial price for a farfetch itiem')
	print(orig_price)
	farfetch_orig_price_text = orig_price.get_text().strip()
	print('\nthis is the orig price get_text')
	print(farfetch_orig_price_text)
	# print(orig_price)

	#discounted price 
	disc_price = soup.select('#slice-pdp > div > div._c84e0a > div._715521 > div._844eda > div > strong')
	farfetch_disc_price_text = disc_price[0].get_text().strip()
	print(farfetch_disc_price_text)

	#this will get the name of the item
	name = soup.find('span', {'class': '_b4693b'})
	farfetch_name_text = name.get_text().strip()
	print(farfetch_name_text)

	#this will get the image src for item
	image = soup.find('img', {'class': '_221e30'})
	farfetch_image_src = image['src']
	print(farfetch_image_src)

	item_object_farfetch = models.Item(url = farfetch_url, name = farfetch_name_text, image =farfetch_image_src, original_price = farfetch_orig_price_text, disc_price = farfetch_disc_price_text, notif_preference = '25')
	#turn into dict before creating record in db
	item_dict_farfetch = model_to_dict(item_object_farfetch)
	#create the new item with payload info
	item = models.Item.create(
		**item_dict_farfetch
	)

	#turn to dict before sending response
	item_dict = model_to_dict(item)
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














