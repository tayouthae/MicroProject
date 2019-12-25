import re
import config

from robobrowser import RoboBrowser

def loginPart(url = "http://classroom.dwit.edu.np"):

    br = RoboBrowser()
    br.open(url)
    form = br.get_form()

    form['username']= config.username
    form['password']= config.password

    br.submit_form(form)

    src = str(br.parsed())

    return src

loginPart()
