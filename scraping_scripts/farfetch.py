import bs4 as bs
# import requests
import urllib.request
#this is the Url we will scrape 
sauce = urllib.request.urlopen('https://www.farfetch.com/shopping/men/prada-palm-print-shirt-item-14752178.aspx').read()

#Load the plain html data into a variable
soup = bs.BeautifulSoup(sauce, 'html.parser')

#this gets the original price for and if applicable discounted price of an item on farfetch
price = soup.find('div', {'class': '_844eda'})
print(price.text.strip())

#this will get the name of the item
name = soup.find('span', {'class': '_b4693b'})
print(name.text.strip())

#this will get the image src for item
image = soup.findAll('img', {'class': '_221e30'})
print(image[0])
