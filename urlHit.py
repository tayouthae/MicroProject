import OLDlogin
import bs4_parsing
import re
from bs4 import BeautifulSoup   
    
count = len(bs4_parsing.exact)

for i in range(count):

    src = OLDlogin.loginPart(bs4_parsing.exact[i])
    
    soup = BeautifulSoup(src, 'lxml')

    header = soup.find('div',{'class':'eventlist my-1'})

    print("\n")
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
    print("\n")
    
    



