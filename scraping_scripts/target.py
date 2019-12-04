import bs4 as bs

import urllib.request

#url to be scraped / will later change to a variable that will hold url user inputs
target_url = ('https://www.target.com/p/samsung-32-class-720p-60-motion-rate-smart-hd-tv-m4500/-/A-51784506')
sauce = urllib.request.urlopen(target_url).read()

#load all html in variable
soup = bs.BeautifulSoup(sauce, 'html.parser')

#scrapes price
name = soup.find('h1', {'class': 'h-margin-b-none h-margin-b-tiny h-text-bold Heading__StyledHeading-sc-6yiixr-0 jHwOVX'})
name_text = name.get_text()
print(name_text)

#scrapes item name 

#scraps image for item

#