# A binary file "Book.dat" has structure [BookNo, Book_Name, Author, Price].
# i. Write a user defined function createFile() to input data for a record and add to Book.dat.
# ii. Write a function countRec(Author) in Python which accepts the Author name as parameter and count
# and return number of books by the given Author are stored in the binary file "Book.dat"


import pickle


def createFile():
    file = open("book.dat", "ab")
    BookNo = int(input("Enter book number: "))
    Book_Name = input("Enter book Name: ")
    Author = input("Enter author: ")
    Price = int(input("Enter price: "))
    record = [BookNo, Book_Name, Author, Price]
    pickle.dump(record, file)
    file.close()


def countRec(Author):
    file = open("book.dat", "rb")
    count = 0
    while True:
        record = pickle.load(file)
        if record[2] == Author:
            count += 1
    file.close()
    return count


def testProgram():
    while True:
        createFile()
        choice = input("Add more record (y/n)? ")
        if choice in 'Nn':
            break
    Author = input('Enter author name to search: ')
    n = countRec(Author)
    print("No of books are", n)


testProgram()
