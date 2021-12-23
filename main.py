from modules.menu import Menu



menu = Menu()
menu.check_for_root()
filename = 'database.json'
key = 'pass.key'


choice = menu.menu()
while choice != 'Q':
  if choice == '1':
    interface.create(filename, key)
  if choice == '2':
    interface.retrieve_data(filename, key)
  if choice == '3':
    interface.delete(filename, key)
  if choice == 'q' or choice == 'Q':
        exit()
  else:
    choice = menu.menu()

exit()
