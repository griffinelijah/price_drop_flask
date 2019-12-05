import bs4 as bs
# import requests
import urllib.request
import sqlite3
conn = sqlite3.connect('price_drop.sqlite', check_same_thread=False)
curs = conn.cursor()

etsy_url = ('https://www.etsy.com/listing/159233019/vintage-pair-of-boehm-canada-geese-hand?ref=pla_similar_listings_top_ad-3&plkey=71f3b193b267baec86e45b9cdd039b415275a63b%3A159233019')

sauce = urllib.request.urlopen(etsy_url).read()

soup = bs.BeautifulSoup(sauce, 'html.parser')

#ths wll get us the original price on etsy
orig_price = soup.find('span', {'class': 'text-largest strong override-listing-price'})
print(orig_price.text.strip())

#this gets us thee naem of the item
name = soup.select('#listing-page-cart > div.pt-xs-1.pr-xs-2.pb-xs-2.pl-xs-2.p-md-0.bg-white.buy-box-toolkit > div.listing-page-title-component > h1')

print(name[0].text.strip())

#this gets us the image
image = soup.find('img', {'class': 'max-width-full horizontal-center vertical-center carousel-image'})
print(image['src'])