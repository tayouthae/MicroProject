import login

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(login.src, 'lxml')
print(soup.title)

#links = soup.find_all("a")
#links = soup.find_all("h6")

links = soup.find_all('div', class_= "event")

print(links)
urls = []

for div in links:
    div.find('a')['href']
    print(div.text)

    #if div is not None and 'href' in div.attrs:
     #   asd = div.get('href')
      #  urls.append(asd)
    


#for link in links:
 #   if "Dashboard" in link.text:
  #      courses = requests.get(link.attrs['href'])

#src = courses.content

#soup2 = BeautifulSoup(src, 'lxml')

#print(urls)

