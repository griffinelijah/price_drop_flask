import bs4 as bs

import urllib.request

#url to be scraped / will later change to a variable that will hold url user inputs
target_url = ('https://www.target.com/p/vizio-d-series-40-class-39-50-diag-1080p-full-array-led-smart-hdtv-d40f-g9/-/A-53855744')
sauce = urllib.request.urlopen(target_url).read()

#load all html in variable
soup = bs.BeautifulSoup(sauce, 'html.parser')

#scrapes price

#scrapes item name 
name = soup.find('h1', {'class': 'h-margin-b-none h-margin-b-tiny h-text-bold Heading__StyledHeading-sc-6yiixr-0 jHwOVX'})
name_text = name.get_text()
print(name_text)

#scraps image for item
image = soup.find('img')
image_src = image['src']
print(image_src)
#