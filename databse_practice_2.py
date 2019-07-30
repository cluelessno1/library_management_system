import sys #this allows you to use the sys.exit command to quit/logout of the application
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
engine = create_engine('sqlite:///library.db', echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Book(Base):
   __tablename__ = 'books'
   id = Column(Integer, primary_key=True)
   name = Column(String)
   author = Column(String)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()

def add_record():
    book_name = input("Enter the book name :")
    book_author = input("Enter the book author :")
    session.add(Book(name = book_name, author = book_author))
    session.commit()
    main_menu()



def main_menu():
    print("####### Main Menu #########")
    print()
    choice = input("1. Add a record\n2. Display all records\n3. Exit\nEnter your choice:")
    if choice == '1': ###The input is being taken as a string, if we write 1 insted of '1', it will not work.
        add_record()
    elif choice == '2':
        display_records()
    elif choice == '3':
        sys.exit()
    else:
        print("The valid inputs are 1,2 and 3 only.\nPlease try again.")
        main_menu()

main_menu()
