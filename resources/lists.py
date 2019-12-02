import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import current_user

lists = Blueprint('lists', 'lists')

#create route for a new list
@lists.route('/', methods=['POST'])
def create_list():
	#this will take the info from the payload to create a new post
	payload = request.get_json()
	new_list = models.List.create(
		title=payload['title'],
		user_id=current_user.id
	)
	#turn into dict before returning object
	new_list_dict = model_to_dict(new_list)
	return jsonify(data=new_list_dict, status={'code': 201, 'message':'successfully created list'}), 201

#display all lists belonging to logged in user
@lists.route('/myLists', methods=['GET'])
def current_users_lists():
	#look for all lists that have a userid matching the logged in users id
	try:
		this_users_list_instances = models.List.select().where(models.List.user_id == current_user.id)
		#turn all posts found into arr of dicts
		this_users_list_dicts = [model_to_dict(lists) for lists in this_users_list_instances]
		return jsonify(data=this_users_list_dicts, status={'code': 200, 'message': 'successfully retrieved all of your lists'}), 200

	except models.DoesNotExist:
		return jsonify(data={}, status={'code': 401, 'message': 'error retrieving lists'}), 401