import OLDlogin

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(OLDlogin.src, 'lxml')
#print(soup.title)

links = soup.find_all('div', {'class':'date'})

#print(links)

url=[]
exact = []

for aTag in links:
    hrefTag = aTag.find('a')
    url.append(hrefTag.get('href'))

for num in url:
    if num not in exact:
        exact.append(num)

print(exact)

