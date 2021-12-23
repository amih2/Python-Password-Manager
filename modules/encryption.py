import os.path
import string
import secrets
import json
from cryptography.fernet import Fernet
from random_username.generate import generate_username

class DataGenerator:
	

	def __init__(self):
		self.alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits
		self.punctuation = string.punctuation

	def generate_random_username(self):
		uname = ''
		return uname.join(generate_username())

	def generate_random_string(self, length, alphabet):
	    return ''.join(secrets.choice(alphabet) for x in range(length))


class FernetCryptography:


	def generate_private_key(self):
		return Fernet.generate_key()

	def save_private_key(self,filename, key):
		with open(filename,'wb') as key_file:
			key_file.write(key)

	def get_private_key(self, filename):
		return open(filename,'rb').read()

	def encrypt_data(self, data, key):
		return key.encrypt(data)

	def get_encrypted_data(self, filename, website, data):
		with open(filename, 'r') as jdata:
			jfile = json.load(jdata)
			string = bytes.fromhex(jfile[website][data])
			return string

	def decrypt_data(self, data, key):
		return key.decrypt(data)
	



