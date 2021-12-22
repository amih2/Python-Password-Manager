import json
import os  

class Database:

	
	def create_database(self, website, uname, passwd, url, filename):
		fname = {website:{}}
		fname[website]["user name"] = uname
		fname[website]["password"] = passwd
		fname[website]["url"] = url
		with open(filename, 'a' ) as json_file:
			json.dump(fname,json_file,sort_keys=False, indent=4)

	def append_to_database(self, website, uname, passwd, url, filename):
		with open(filename, 'r') as jsondata:  
			fname = json.load(jsondata)
			fname[website] = {}
			fname[website]["user name"] = uname
			fname[website]["password"] = passwd
			fname[website]["url"] = url
			with open(filename, 'w') as jsondata:
				json.dump(fname, jsondata, sort_keys=False, indent=4)

	def list_websites(self, filename):
		if os.path.isfile(filename):
			with open(filename, 'r') as jsondata:
				pass_list = json.load(jsondata)
			passwords_lst = ""
			for i in pass_list:
				passwords_lst += "--{}\n".format(i)
			return passwords_lst
		else:
			print("You have no saved passwords ")
			exit()

	def delete_password(self, website, filename):
		with open(filename, 'r') as jdata:
			jfile = json.load(jdata)
			jfile.pop(website)
			with open(filename, 'w') as jdata:
				json.dump(jfile, jdata, sort_keys=True, indent=4)

	def delete_database(self, filename):
		return os.remove(filename)
