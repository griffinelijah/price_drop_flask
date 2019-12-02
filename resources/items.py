import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import current_user

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

#get a lists items
@items.route('/<listId>', methods=['GET'])
def get_lists_items(listId):
	try:
		#query for all items that belong to the postid being passed in the uurl
		items = [model_to_dict(items) for items in models.Item.select().where(models.Item.list_id == listId)]
		return jsonify(data=items, status={'code': 200, 'message': 'Successfully retreived all items'}), 200
	except models.DoesNotExist:
		return jsonify(data={}, status={'code': 401, 'message': 'Error retrieving resources'}), 401

@items.route('/<itemId>', methods=['DELETE'])
def delete_item(itemId):
	#query for item that matches id
	item_to_delete = models.Item.get_by_id(itemId)
	print('\nthis is item_to_delete')
	print(item_to_delete)
	item_to_delete.delete_instance()
	return jsonify(data={}, status={'code': 200, 'message': 'Successfully delete item'})














