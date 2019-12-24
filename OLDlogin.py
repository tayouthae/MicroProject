import re
import config

from robobrowser import RoboBrowser

br = RoboBrowser()
br.open("http://classroom.dwit.edu.np")
form = br.get_form()

form['username']= config.username
form['password']= config.password

br.submit_form(form)

src = str(br.parsed())
