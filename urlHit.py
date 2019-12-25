import OLDlogin
import bs4_parsing
import re
from bs4 import BeautifulSoup
import json
    
count = len(bs4_parsing.exact)

tempdict = {}
combine = {}

for i in range(count):

    src = OLDlogin.loginPart(bs4_parsing.exact[i])
    
    soup = BeautifulSoup(src, 'lxml')

    header = soup.find('div',{'class':'eventlist my-1'})

    print("\n")
    for names in header.find_all('h3'):
        tempdict.update({'header': names.text})
        print(names.text)

    try:
        for names in header.find_all('p'):
            tempdict.update({'paragraph': names.text})
            print(names.text)
    except:
        tempdict.update({'paragraph': None})
        print("No paragraph")

    counttemp = 0    
    for names in header.find_all('a'):
        if "activity" in names.text:
            counttemp +=1
            continue
        else:
            tempdict.update({'aTag %d' %counttemp : names.text})
            print(names.text)
            counttemp +=1
    print("\n")

    combine.update({i : tempdict})

combine.update({'UserName': bs4_parsing.userName})
print(tempdict)
print("\n")
print(combine)

JSONfile = json.dumps(combine)

with open("D:\BOOKS\SEMESTER 5\Micro Project\Scrap\data.txt","w") as file:
    file.write(JSONfile)


