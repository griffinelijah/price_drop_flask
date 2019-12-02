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

