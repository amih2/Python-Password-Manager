from cryptography.fernet import Fernet
import os.path
from modules.database import Database
from modules.encryption import DataGenerator, FernetCryptography
from modules.superuser import Superuser
from modules.clipboard import ClipBoard
from colorama import Fore, Style

class Menu:
  

  def __init__(self):
    self.password = DataGenerator()
    self.username = DataGenerator()
    self.database = Database()
    self.crypto = FernetCryptography()
    self.root = Superuser()
    self.copy = ClipBoard()

  def check_for_root(self):
    if self.root.is_root() == False:
      print(Fore.RED + "ACCESS DENIED!")
      print("This program is suposed to be run with super user privileges. Run this program as a root")
      Style.RESET_ALL
      exit()

  def menu(self):
    print('-'*30)
    print(('-'*13) + 'Menu'+ ('-' *13))
    print('1. Generate random new password')
    print('2. Retrieve a password')
    print('3. Delete password or whole database')
    print('[Q/q]. Exit')
    print('-'*30)
    return input(': ')

  def create(self, filename, key):
    print("Please proivide the name of the site or app you want to generate a password for")
    website = input()
    print("do you want to automaticly generate userame?(y/n)")
    uname = input()
    if uname == 'y' or uname == 'Y':
        username = self.username.generate_random_username().encode("utf-8")
    else:
        username = self.username.create_uname().encode("utf-8")
    print("Put url of a platform")
    url = input().encode("utf-8")
    print("Do you want punctuation included in your password? (y/n)")
    includePunctuation = input()
    print("Please enter the length of your password")
    length = int(input())
    alphabet = self.password.alphabet
    if includePunctuation == 'y' or includePunctuation == 'Y':
      alphabet += self.password.punctuation
    plainText = self.password.generate_random_string(length, alphabet).encode("utf-8")
    generateKey = self.crypto.generate_private_key()
    if not os.path.exists(key):
      self.crypto.save_private_key(key, generateKey)
    retrievedKey = self.crypto.get_private_key(key)
    privateKey = Fernet(retrievedKey)
    uname = self.crypto.encrypt_data(username, privateKey)
    URL = self.crypto.encrypt_data(url,privateKey)
    passwd = self.crypto.encrypt_data(plainText, privateKey)
    hexUname = uname.hex()
    hexUrl = URL.hex()
    hexPass = passwd.hex()
    if os.path.exists(filename):
      self.database.append_to_database(website,hexUname,hexPass,hexUrl,filename)
    else:
      self.database.create_database(website,hexUname,hexPass,hexUrl,filename)
      self.root.chmod(key, 0o600)                  #0o is a prefix that python3 requires for permission manipulation
      self.root.chmod(filename, 0o600)
      self.root.chown(key, 0, 0)                 #0 == root
      self.root.chown(filename, 0, 0) 
  
  def retrieve_data(self, filename, key):
    print(self.database.list_websites(filename))
    print("Enter website name or app name to retrieve a password: ")
    website = input()
    key = self.crypto.get_private_key(key)
    privateKey = Fernet(key)
    encryptedUname = self.crypto.get_encrypted_data(filename,website,'user name')
    encryptedUrl = self.crypto.get_encrypted_data(filename,website,'url')
    encryptedPass = self.crypto.get_encrypted_data(filename,website, 'password')
    url = encryptedUrl
    uname = encryptedUname
    passwd = encryptedPass
    decryptedUrl = self.crypto.decrypt_data(url, privateKey)
    decryptedPass = self.crypto.decrypt_data(passwd, privateKey)
    decryptedUname = self.crypto.decrypt_data(uname, privateKey)
    print("Username: ", Fore.GREEN + decryptedUname.decode('utf-8'))
    print(Style.RESET_ALL)
    print("Password: ", Fore.GREEN + decryptedPass.decode('utf-8'))
    print(Style.RESET_ALL)
    print("Website: ", Fore.GREEN + decryptedUrl.decode('utf-8'))
    print(Style.RESET_ALL)
    print("Copy password to clipboard? [y/n]")
    copyToClipboard = input()
    if copyToClipboard == 'y' or copyToClipboard == 'Y':
      self.copy.set_clipboard_data(decryptedPass)

  def delete(self, filename, key):
    if os.path.exists(filename) or os.path.exists(key):
      print("Do you want to delete only one password or whole database?: [1]Password, [2]Database ")
      indite = int(input())
      if indite == 1:
        print(self.database.list_websites(filename))
        print("Enter a website you want to delete:")
        website = input()
        print("Are you sure you want to delete the password? [y/n]")
        deletePass = input()
        if deletePass == 'y' or deletePass == 'Y':
          self.database.delete_password(website,filename)
        else:
          exit()
      if indite == 2:
        print("Are you sure you want to delete whole database: [y/n]")
        deleteData = input()
        if deleteData == 'y' or deleteData == 'Y':
          self.database.delete_database(filename)
          self.database.delete_database(key)
    else:
      print("No database has been found")
      exit()



