from modules.menu import Menu



interface = Menu()
interface.check_for_root()
filename = 'database.json'
key = 'pass.key'


choice = interface.menu()
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
    choice = interface.menu()

exit()
