import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

lists = Blueprint('lists', 'lists')

#create route for a new list
@lists.route('/', methods=['POST'])
@login_required
def create_list():
	#this will take the info from the payload to create a new post
	payload = request.get_json()
	new_list = models.List.create(
		title=payload['title'],
		user_id=current_user.id,
		notif_preference=payload['notif_preference']
	)
	#turn into dict before returning object
	new_list_dict = model_to_dict(new_list)
	new_list_dict['user'].pop('password')
	return jsonify(data=new_list_dict, status={'code': 201, 'message':'successfully created list'}), 201
#display all lists belonging to logged in user
@lists.route('/myLists', methods=['GET'])
@login_required
def current_users_lists():
	#look for all lists that have a userid matching the logged in users id
	try:
		this_users_list_instances = models.List.select().where(models.List.user_id == current_user.id)
		#turn all posts found into arr of dicts


		this_users_list_dicts = [model_to_dict(lists) for lists in this_users_list_instances]
		return jsonify(data=this_users_list_dicts, status={'code': 200, 'message': 'successfully retrieved all of your lists'}), 200

	except models.DoesNotExist:
		return jsonify(data={}, status={'code': 401, 'message': 'error retrieving lists'}), 401

@lists.route('/<id>', methods=['PUT'])
@login_required
def update_post(id):
	payload = request.get_json()
	#find list that matches id being passed through
	list_to_update = models.List.get_by_id(id)

	#check to make list's user id matches logged in user(this should not happen as only posts that belong to a certain user are being displayed)
	if(list_to_update.user.id == current_user.id):
		list_to_update.title = payload['title'] if 'title' in payload else none
		list_to_update.notif_preference = payload['notif_preference'] if 'notif_preference' in payload else none

		list_to_update.save()
		list_dict = model_to_dict(list_to_update)

		#remove pw before returning response
		list_dict['user'].pop('password')
		return jsonify(data=list_dict, status={'code': 200, 'message': 'list successfully updated'}), 200

	else:
		return jsonify(data='Foribdden', status={'code': 403, 'message': 'You must be the owner of this list to update it'}), 403
	return jsonify(data=list_dict, status={'code': 200, 'message': 'list successfully updated'}), 200


#delete a list
@lists.route('/<id>', methods=['DELETE'])
@login_required
def delete_post(id):
	#find post that matches the id being passed through 
	list_to_delete = models.List.get_by_id(id)
	print(list_to_delete)
	#check to make sure that user trying to delete owns the post(this should not happen as only posts that belong to a certain user are being displayed)
	if list_to_delete.user.id != current_user.id:
		return jsonify(data='Forbidden', status={'code': 403, 'message': 'You must be the owner of this list to delete it'}), 403
	#else if they do own the list
	else:
		list_to_delete.delete_instance()
	return jsonify(data={}, status={'code': 200, 'message': 'resource successfully deleted'}), 200	















