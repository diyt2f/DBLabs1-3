import psycopg2
import Model

def display(text):
    print(text)

def input_many():
    input1 = input('Input (delimiter=="/"): ')
    input1 = input1.split('/')
    return input1

def display_author(result):
    try:
        print('READ:')
        print('AuthorID:', result[0])
        print('Author Name:', result[1])
    except:
        print("Can't display author.")

def display_book(result):
    try:
        print('READ:')
        print('BookID:', result[0])
        print('Book Name:', result[1])
        print('Book Page Count:', result[2])
        print('Book Price:', result[3])
    except:
        print("Can't display book.")

def display_purchase(result):
    try:
        print('READ:')
        print('PurchaseID:', result[0])
        print('Purchase Price:', result[1])
        print('Purchase Transaction Number:', result[2])
        print('Purchase ClientID:', result[3])
    except:
        print("Can't display purchase.")

def display_client(result):
    try:
        print('READ:')
        print('ClinetID:', result[0])
        print('Clinet Name:', result[1])
        print('Client Login:', result[2])
        print('Client Email:', result[3])
    except:
        print("Can't display client.")

def display_books(result):
    try:
        print('READ:')
        for i in result:
            print('BookID:', i[0], ', BookName: ', i[1], ', PageCount:', i[2], ', Price:', i[3])
    except:
        print("Can't display books.")

def display_books1(result):
    try:
        print('READ:')
        for i in result:
            print('Book is ',)
    except:
        print("Can't display books.")

def display_authors(result):
    try:
        print('READ:')
        for i in result:
            print('AuthorID: ', i[0], ', Name: ', i[1])
    except:
        print("Can't display authors.")


