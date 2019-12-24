import bs4_parsing
import re
import config
from bs4 import BeautifulSoup

from robobrowser import RoboBrowser

br = RoboBrowser()

count = len(bs4_parsing.exact)

for i in range(count):
    
    br.open(bs4_parsing.exact[i])
    form = br.get_form()

    form['username']= config.username
    form['password']= config.password
    br.submit_form(form)

    src = str(br.parsed())
    
    soup = BeautifulSoup(src, 'lxml')

    header = soup.find_all('div',{'class':'eventlist my-1'})

    for names in header:
        Text = names.find('h3')
        print(Text.get_text())
        Text2 = names.find('a')
        print(Text2.get_text())
