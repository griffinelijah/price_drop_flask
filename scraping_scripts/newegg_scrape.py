import bs4 as bs
# import requests
import urllib.request
#this is the Url we will scrape 
sauce = urllib.request.urlopen('https://www.farfetch.com/shopping/men/a-cold-wall-faded-effect-logo-print-hoodie-item-13790443.aspx?storeid=9306').read()

#Load the plain html data into a variable
# plain_html = requests.get(sauce)
soup = bs.BeautifulSoup(sauce, 'html.parser')

#parse the html
# soup = BeautifulSoup(plain_html.text, 'html.parser')
# print(soup)

#this gets the original price for and if applicable discounted price of an item on farfetch
price = soup.find('div', {'class': '_844eda'})
print(price.text.strip())

title = soup.find('span', {'class': '_b4693b'})
print(title.text.strip())

# image = soup.findAll('img')
# print(image)
image = soup.findAll('img', {'class': '_221e30'})
print(image)

# for img in soup.findAll('img', )