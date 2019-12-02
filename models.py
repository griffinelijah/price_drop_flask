import datetime
from peewee import *
from flask_login import UserMixin

DATABASE = SqliteDatabase('price_drop.sqlite')

class User(UserMixin, Model):
	email = CharField(unique = True)
	password = CharField()
	created_date = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = DATABASE

class List(Model):
	title = CharField()
	user_id = ForeignKeyField(User, backref='lists')
	created_date = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = DATABASE

class Item(Model):
	url = CharField()
	image = CharField()
	original_price = CharField()
	disc_price = CharField()
	notif_preference = CharField()
	created_date = DateTimeField(default=datetime.datetime.now)
	list_id = ForeignKeyField(List, backref='items')

	class Meta:
		database = DATABASE

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, List, Item], safe=True)
	print('TABLES CREATED')
	DATABASE.close()
