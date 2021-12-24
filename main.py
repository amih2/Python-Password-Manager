from modules.menu import Menu



menu = Menu()
menu.check_for_root()
database = 'database.json'
key = 'pass.key'


choice = menu.menu()
while choice != 'Q':
  if choice == '1':
    menu.create(database, key)
  if choice == '2':
    menu.retrieve_data(database, key)
  if choice == '3':
    menu.delete(database, key)
  if choice == 'q' or choice == 'Q':
        exit()
  else:
    choice = menu.menu()

exit()
