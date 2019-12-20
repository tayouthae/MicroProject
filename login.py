import re
import key
from cryptography.fernet import Fernet

from robobrowser import RoboBrowser

br = RoboBrowser()
br.open("http://classroom.dwit.edu.np/my/")
form = br.get_form()

#decrypt
file = open('key.key','rb')
new_key = file.read()
f2 = Fernet(new_key)


username = key.encrypted
password = key.encrypted_pass

decrypted = f2.decrypt(username)
decrypted_pass = f2.decrypt(password)

form['username']= decrypted
form['password']= decrypted_pass
br.submit_form(form)

src = str(br.parsed())

start = '<span class="usertext mr-1">'
end = '</span>'

result = re.search('%s(.*)%s' % (start, end), src).group(1)

print(result)

