from bs4 import BeautifulSoup
import requests

#this is the Url we will scrape 
sauce = 'https://www.newegg.com/msi-radeon-rx-570-rx-570-armor-8g-oc/p/N82E16814137256?Item=N82E16814137256'

#Load the plain html data into a variable
plain_html = requests.get(sauce)

#parse the html
soup = BeautifulSoup(plain_html.text, 'html.parser')

# print(soup)

item_container = soup.find('div', {'class': 'grpArticle'})
# print(item_container)

item_title = item_container.find('span', {'id': 'grpDescrip_14-137-256'})
print(item_title.text.strip())