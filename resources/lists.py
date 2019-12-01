import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

lists = Blueprint('lists', 'lists')

#create route for a new list
@lists.route('/', methods=['POST'])
def create_list():
	#this will take the info from the payload to create a new post
	payload = request.get_json()
	list = models.List.create(
		title=payload['title'],
		user_id=1,
		list_id=1
	)
	#turn into dict before returning object
	list_dict = model_to_dict(list)
	return jsonify(data=list_dict, status={'code': 201, 'message':'successfully created list'}), 201

	