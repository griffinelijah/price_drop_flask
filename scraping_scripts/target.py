import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://www.target.com/p/tcl-43-roku-4k-uhd-hdr-smart-tv-43s425/-/A-52177069').read()

soup = bs.BeautifulSoup(sauce, 'html.parser')

#not finding correct span with price
price = soup.find('span', {'class': 'h-padding-b-default'})
# print(price)
