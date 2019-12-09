import sqlite3
import datetime
from peewee import *
from flask_login import UserMixin
from scraping_scripts.farfetch import *
from scraping_scripts.target import *
from scraping_scripts.etsy import *
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
	notif_preference = CharField()
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
	created_date = DateTimeField(default=datetime.datetime.now)
	list_id = ForeignKeyField(List, backref='items')

	class Meta:
		database = DATABASE

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, List, Item], safe=True)
	print('TABLES CREATED')

	#this will be used to create a target item
	# item_object_target = Item(url = target_url, name = target_name_text, image = target_image_src, original_price = target_orig_price_text, disc_price = target_disc_price_text, notif_preference = '25')

	# item_dict_target = model_to_dict(item_object_target)
	# Item.create(**item_dict_target)

	#this will create our etsy
	# item_object_etsy = Item(url = etsy_url, name = etsy_name_text,
	# 	image = etsy_image_src, original_price = etsy_orig_price_text, disc_price = etsy_orig_price_text, notif_preference = '25')

	# item_dict_etsy = model_to_dict(item_object_etsy)
	# Item.create(**item_dict_etsy)

	DATABASE.close()























