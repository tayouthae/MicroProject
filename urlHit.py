import bs4_parsing
import re
import config
from bs4 import BeautifulSoup

from robobrowser import RoboBrowser

def loginPart(url):

    br = RoboBrowser()    
    br.open(url)
    form = br.get_form()

    form['username']= config.username
    form['password']= config.password
    br.submit_form(form)

    src = str(br.parsed())
    
    soup = BeautifulSoup(src, 'lxml')

    header = soup.find('div',{'class':'eventlist my-1'})

    for names in header.find_all('h3'):
        print(names.text)

    try:
        for names in header.find_all('p'):
            print(names.text)
    except:
        print("No paragraph")
        
    for names in header.find_all('a'):
        if "activity" in names.text:
            continue
        else:
            print(names.text)


count = len(bs4_parsing.exact)

for i in range(count):
    
    loginPart(bs4_parsing.exact[i])
    
    



