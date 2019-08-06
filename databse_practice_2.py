import sys #this allows you to use the sys.exit command to quit/logout of the application
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy import text #For using SQL text based commands in Quesry statements



engine = create_engine('sqlite:///library.db', echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Book(Base):
   __tablename__ = 'books'
   id = Column(Integer, primary_key=True) # Every SQLAlchemy table should have a primary key named 'id'
   isbn = Column(Integer)
   name = Column(String)
   author = Column(String)
   publisher = Column(String)
   quantity = Column(Integer)
   checked_out = Column(Integer)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()


def update_record(book_isbn):
    print("Have to make this")
    main_menu()

def check_isbn(): ##To check if the length of the inputted ISBN is 10 or 13 and whther such an ISBN already exists.
    book_isbn = input("Enter ISBN number of the book :")
    if len(book_isbn)!=10:
        if len(book_isbn)!=13:
            print("ISBN is 10 or 13 digit number, please enter it correctly again")
            print(book_isbn)
            check_isbn()
    result = session.query(Book).all()
    flag = False
    for row in result:
        if row.isbn == int(book_isbn):
            flag = True
            break
    if flag: #If written while flag: it gave logical error on execution. The value of book_isbn became fixed at the first eneterd value,
        print("The record with this ISBN already exists.\nEnter a new record or modify data of existing record.")
        while True:
            choice = int(input("1. Enter new record\n2. Modify existing record\n3. Main Menu\n Enter your choice: "))
            if choice == 1:
                check_isbn()
                break
            elif choice == 2:
                update_record(int(book_isbn)) #Have to create this function.
                break
            elif choice == 3:
                main_menu()
                break
            else:
                print("Entered invalid option.\nPlease enter once again.")

    return book_isbn


def add_record():
    book_isbn = check_isbn()
    book_name = input("Enter the book name :")
    book_author = input("Enter the book author :")
    book_publisher = input("Enter the publisher of the book :")
    book_quantity = input("Enter the total no. of books being added to the library :")
    session.add(Book(isbn = int(book_isbn), name = book_name, author = book_author, publisher = book_publisher, quantity = int(book_quantity)))
    session.commit()
    main_menu()

def display_records():
    print("1. Display details of all books\n2. Search books by ISBN\n3. Search books by book name\n4. Search books by author\n5. Go back to main menu :")
    choice = input("Enter you choice :")
    if choice == '1':
        result = session.query(Book).from_statement(text("SELECT * FROM books")).all()
        print("\n")
        for row in result:
            print("ISBN: ", row.isbn, "Book Name: ", row.name, "Author:", row.author, "Publisher :", row.publisher, "Quantity :", row.quantity, "Checked Out :", row.checked_out)
        print("\n")
        main_menu()
    elif choice == '2':
         book_isbn = input("Enter ISBN number of the book :")
         result = session.query(Book).filter(Book.isbn == int(book_isbn))
         print("\n")
         for row in result:
            print("ISBN: ", row.isbn, "Book Name: ", row.name, "Author:", row.author, "Publisher :", row.publisher, "Quantity :", row.quantity, "Checked Out :", row.checked_out)
         print("\n")
         main_menu()
    elif choice == '3':
        book_name = input("Enter title of the book :")
        result = session.query(Book).filter(Book.name == book_name)
        print("\n")
        for row in result:
            print("ISBN: ", row.isbn, "Book Name: ", row.name, "Author:", row.author, "Publisher :", row.publisher, "Quantity :", row.quantity, "Checked Out :", row.checked_out)
        print("\n")
        main_menu()
    elif choice == '4':
        book_author = input("Enter author of the book :")
        result = session.query(Book).filter(Book.author == book_author)
        print("\n")
        for row in result:
            print("ISBN: ", row.isbn, "Book Name: ", row.name, "Author:", row.author, "Publisher :", row.publisher, "Quantity :", row.quantity, "Checked Out :", row.checked_out)
        print("\n")
        main_menu()
    elif choice == '5':
        main_menu()
    else:
        print("Entered invaild input. Please enter the input again.")
        display_records()


def main_menu():

    print("####### Main Menu #########")
    print()
    choice = input("1. Add record\n2. Display record\n3. Exit\nEnter your choice:")

    # Add a delete record and update record to complete the first part
    # After that try and create a table members/memberships and try to integrate that with the table Book
    # Try and add an interface to borrow books(change Checked Out value)
    # After all that is done, learn how to navigate to different windows in Tkinter
    # After that try and migrate your database system to GUI

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
