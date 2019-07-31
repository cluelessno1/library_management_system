import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

choice = input("1. Add a record\n2. Display all records\n3. Exit\nEnter your choice:")

if choice == 1:
    print("integer")
elif choice == '1':
    print("string")
elif choice == '2':
    cls()
else:
    print("undefined")