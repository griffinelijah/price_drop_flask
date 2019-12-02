import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

items = Blueprint('items', 'items')

#create route for items
@items.route('/<listId>', methods=['POST'])
def create_item(listId):
	payload = request.get_json()
	#query for List to add item to
	found_list = models.List.get_by_id(listId)
	#create the new item with payload info
	item = models.Item.create(
		url = payload['url'],
		image = payload['image'],
		original_price = payload['original_price'],
		disc_price = payload['disc_price'],
		notif_preference = payload['notif_preference'],
		list_id = found_list.id
	)

	#turn to dict before sending response
	item_dict = model_to_dict(item)
	print(item_dict)
	return jsonify(data=item_dict, status={'code': 201, 'message': "Successfully created item"}), 201
