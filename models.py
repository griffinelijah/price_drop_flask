import os
import sqlite3
import datetime
from peewee import *
from flask_login import UserMixin
from scraping_scripts.farfetch import *
from scraping_scripts.target import *
from scraping_scripts.etsy import *
from playhouse.shortcuts import model_to_dict
from playhouse.db_url import connect

if 'ON_HEROKU' in os.environ:
  DATABASE = connect(os.environ.get('DATABASE_URL')) 
else:
  DATABASE = SqliteDatabase('price_drop.sqlite')

  # OPTIONALLY: instead of the above line, here's how you could have your 
  # local app use PSQL instead of SQLite:

  # DATABASE = PostgresqlDatabase('dog_demo', user='reuben')  

  # the first argument is the database name -- YOU MUST MANUALLY CREATE 
  # IT IN YOUR psql TERMINAL
  # the second argument is your Unix/Linux username on your computer


class User(UserMixin, Model):
	email = CharField(unique = True)
	password = CharField()
	created_date = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = DATABASE

class List(Model):
	user = ForeignKeyField(User, backref='lists')
	title = CharField()
	notif_preference = CharField()
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
	user = ForeignKeyField(User, backref='items')
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























