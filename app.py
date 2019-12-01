from flask import Flask, jsonify, g
from flask_cors import CORS
import models

# from resources.users import users
from resources.lists import lists
# from resources.items import items

from flask_login import LoginManager

DEBUG = True
PORT = 8000


app = Flask(__name__)
#remember to hit this later on for security
app.secret_key = 'fdsafdsfdsa'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userId):
	#this is where we find a matching user in thhe db
	try:
		return models.User.get(models.User.id == userId)
	except models.DoesNotExist:
		return None

@login_manager.unauthorized_handler
def unauthorized():
	return jsonify(data={
		'error': 'user not logged in'
		}, status={
		'code': 401,
		'message': 'You must be logged in to access that resource'
		}), 401

@app.before_request
def before_request():
	g.db = models.DATABASE
	g.db.connect()
	return response

# CORS(users, origins=['http://localhost:3000'], supports_credentials=True)
CORS(lists, origins=['http://localhost:3000'], supports_credentials=True)
# CORS(items, origins=['http://localhost:3000'], supports_credentials=True)

# app.register_blueprint(users, url_prefix='/api/v1/users')
app.register_blueprint(lists, url_prefix='/api/v1/lists')
# app.register_blueprint(items, url_prefix='/api/v1/items')

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
