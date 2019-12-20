from cryptography.fernet import Fernet
from getpass import getpass

key = Fernet.generate_key()

file = open('key.key', 'wb')
file.write(key) # The key is type bytes still


username = input("Enter Username: ")
password = getpass("Password: ")

#to convert msg to bytes
encoded = username.encode()
encoded_pass = password.encode()

#to encrypt

f = Fernet(key)
encrypted = f.encrypt(encoded)
encrypted_pass = f.encrypt(encoded_pass)

file.write(encrypted)
file.write(encrypted_pass)
file.close()
