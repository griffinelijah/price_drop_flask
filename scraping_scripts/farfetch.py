import bs4 as bs
# import requests
import urllib.request
import sqlite3
conn = sqlite3.connect('price_drop.sqlite', check_same_thread=False)
curs = conn.cursor()

#this is the Url we will scrape / will later change to a variable that will hold url user inputs
farfetch_url = ('https://www.farfetch.com/shopping/men/prada-palm-print-shirt-item-14752178.aspx')
sauce = urllib.request.urlopen(farfetch_url).read()

#Load the plain html data into a variable
soup = bs.BeautifulSoup(sauce, 'html.parser')

#this gets the original price for and if applicable discounted price of an item on farfetch
price = soup.find('div', {'class': '_844eda'})
# print(price.text.strip())
price_text = price.get_text()

#this will get the name of the item
name = soup.find('span', {'class': '_b4693b'})
# print(name.text.strip())
name_text = name.get_text()


#this will get the image src for item
image = soup.find('img', {'class': '_221e30'})
# print(image[0])
image_text = image.get_text()










