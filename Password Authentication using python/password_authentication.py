import getpass

database = {'dani': 'dani_dani', 'daniel': 'danie_daniel'}

username = input("Enter your username: ")

if username in database:
  password = getpass.getpass("Enter your password: ")
  while password != database[username]:
    password = getpass.getpass("Incorrect password. Please try again: ")
  print("verified")
else:
  print("You are not registered")
