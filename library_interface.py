import numpy as np

class book_details:
    def __init__(self, title, author, ref_no):
        self.title = title
        self.author = author
        self.ref_no = ref_no


print("\t\t\t*****Library Management System*****")
print("1. Adminsitrator \n2. Student")
choice = input("Enter your choice: ")



"""
title = input("Enter the Title of the book: ")
author = input("Enter the Author of the book: ")

b1 = book_details(title, author)



print(b1.title)
print(b1.author)
"""