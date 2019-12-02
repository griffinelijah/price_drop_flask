import models
from flask import request, jsonify, Blueprint
from playhouse.shortcuts import model_to_dict
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user

users = Blueprint('users', 'users')

#to register a new user into the db
@users.route('/register', methods=['POST'])
def register():
	payload = request.get_json()
	#lowercase all emails to check against db and make sure it is new email being registered each time
	payload['email'].lower()

	try:
		models.User.get(models.User.email == payload['email'])
		return jsonify(data={}, status={'code': 401, 'message': 'A user with that email already exists'}), 401

	#if email is not registered finish registration
	except models.DoesNotExist:
		#encrypt pw 
		payload['password'] = generate_password_hash(payload['password'])

		#create a new user with payload info
		user = models.User.create(**payload)

		#turn to dict and delete pw before sending response
		user_dict = model_to_dict(user)
		del user_dict['password']
		return jsonify(data=user_dict, status={'code': 201, 'message': 'Successfully registered new user'}), 201

#login as existing user
