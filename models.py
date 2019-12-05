import sqlite3
import datetime
from peewee import *
from flask_login import UserMixin
from scraping_scripts.farfetch import *
from playhouse.shortcuts import model_to_dict

DATABASE = SqliteDatabase('price_drop.sqlite')


class User(UserMixin, Model):
	email = CharField(unique = True)
	password = CharField()
	created_date = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = DATABASE

class List(Model):
	title = CharField()
	user = ForeignKeyField(User, backref='lists')
	created_date = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = DATABASE

class Item(Model):
	url = CharField()
	name = CharField()
	image = CharField()
	original_price = CharField()
	disc_price = CharField()
	notif_preference = CharField()
	created_date = DateTimeField(default=datetime.datetime.now)
	list_id = ForeignKeyField(List, backref='items', null=True)

	class Meta:
		database = DATABASE


def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, List, Item], safe=True)
	print('TABLES CREATED')
	#creating item object with data pulled from variables iin the farfetch.py file
	item_object_farfetch = Item(url = farfetch_url, name = farfetch_name_text, image = farfetch_image_src, original_price = farfetch_orig_price_text, disc_price = farfetch_disc_price_text, notif_preference = '25')
	#turn into dict before creating record in db
	item_dict_farfetch = model_to_dict(item_object_farfetch)
	#create db entry in the Item table with spread op info
	Item.create(**item_dict_farfetch)
	# item_object_target = Item(url = target_url, name = name_text,)
	DATABASE.close()
