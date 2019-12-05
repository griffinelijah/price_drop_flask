import bs4 as bs
# import requests
import urllib.request
import sqlite3
conn = sqlite3.connect('price_drop.sqlite', check_same_thread=False)
curs = conn.cursor()

etsy_url = ('https://www.etsy.com/listing/496574883/custom-refillable-leather?ref=hp_prn&pro=1')

sauce = urllib.request.urlopen(etsy_url).read()

soup = bs.BeautifulSoup(sauce, 'html.parser')

#ths wll get us the original price on etsy
orig_price = soup.find('span', {'class': 'text-largest strong override-listing-price'})
etsy_orig_price_text = orig_price.text.strip()
print(etsy_orig_price_text)

#this gets us thee naem of the item
etsy_name = soup.select('#listing-page-cart > div.pt-xs-1.pr-xs-2.pb-xs-2.pl-xs-2.p-md-0.bg-white.buy-box-toolkit > div.listing-page-title-component > h1')
etsy_name_text = etsy_name[0].text.strip()
print(etsy_name_text)

#this gets us the image
etsy_image = soup.find('img', {'class': 'max-width-full horizontal-center vertical-center carousel-image'})
etsy_image_src = etsy_image['src']
print(etsy_image_src)