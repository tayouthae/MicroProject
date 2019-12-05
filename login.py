import re
import config

from robobrowser import RoboBrowser

br = RoboBrowser()
br.open("http://classroom.dwit.edu.np/my/")
form = br.get_form()
form['username']= config.Deerwalk_Username
form['password']= config.Deerwalk_Password
br.submit_form(form)

src = str(br.parsed())

start = '<span class="usertext mr-1">'
end = '</span>'

result = re.search('%s(.*)%s' % (start, end), src).group(1)

print(result)

