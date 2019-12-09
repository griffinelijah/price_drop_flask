# import bs4 as bs
# # import requests
# import urllib.request
# import sqlite3
# conn = sqlite3.connect('price_drop.sqlite', check_same_thread=False)
# curs = conn.cursor()
# from resources.items import *

# #this is the Url we will scrape / will later change to a variable that will hold url user inputs
# # farfetch_url = (payload['url'])

# # sauce = urllib.request.urlopen(farfetch_url).read()

# # #Load the plain html data into a variable
# # soup = bs.BeautifulSoup(sauce, 'html.parser')

# # #this gets the original price for and if applicable discounted price of an item on farfetch
# # orig_price = soup.select('#slice-pdp > div > div._c84e0a > div._715521 > div._844eda > div > span._ffbca2._1fe24a')
# # farfetch_orig_price_text = orig_price[0].get_text().strip()
# # print(farfetch_orig_price_text)

# # #discounted price 
# # disc_price = soup.select('#slice-pdp > div > div._c84e0a > div._715521 > div._844eda > div > strong')
# # farfetch_disc_price_text = disc_price[0].get_text().strip()
# # print(farfetch_disc_price_text)

# # #this will get the name of the item
# # name = soup.find('span', {'class': '_b4693b'})
# # farfetch_name_text = name.get_text().strip()
# # print(farfetch_name_text)

# # #this will get the image src for item
# # image = soup.find('img', {'class': '_221e30'})
# # farfetch_image_src = image['src']
# # print(farfetch_image_src)











