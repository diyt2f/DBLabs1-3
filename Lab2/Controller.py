import psycopg2
import Model
import View

def connect():
    conn = psycopg2.connect("dbname=Lab1BookShop user=postgres password=qwe123")
    cur = conn.cursor()
    return conn, cur

def open_menu():
    while 1:
        i = input('Input: ')
        i = i.upper()
        i = i.split()
        if i[0] == 'READ':
            View.display('Reading...')
            if i[1] == "AUTHOR":
                result = Model.get_author(int(i[2]))
                View.display_author(result)
            elif i[1] == "BOOK":
                result = Model.get_book(int(i[2]))
                View.display_book(result)
            elif i[1] == "PURCHASE":
                result = Model.get_purchase(int(i[2]))
                View.display_purchase(result)
            elif i[1] == "CLIENT":
                result = Model.get_client(int(i[2]))
                View.display_client(result)
            elif i[1] == "BOOKS_BY_PURCHASE_ID":
                result = Model.get_books_by_purchase_id(int(i[2]))
                View.display_books(result)
            elif i[1] == "AUTHORS_BY_BOOK_ID":
                result = Model.get_authors_by_book_id(int(i[2]))
                View.display_authors(result)
        elif i[0] == 'ADD':
            View.display('Adding...')
            if i[1] == "AUTHOR":
                View.display('author_id/author_name')
                input1 = View.input_many()
                View.display(input1)
                Model.add_author(input1[0], input1[1])
            elif i[1] == "BOOK":
                View.display('book_id/book_name/page_count/book_price')
                input1 = View.input_many()
                Model.add_book(input1[0], input1[1], input1[2], input1[3])
            elif i[1] == "PURCHASE":
                View.display('purchase_id/client_id/sum/transaction_number')
                input1 = View.input_many()
                Model.add_purchase(input1[0], input1[1], input1[2], input1[3])
            elif i[1] == "CLIENT":
                View.display('client_id/name/login/email')
                input1 = View.input_many()
                Model.add_client(input1[0], input1[1], input1[2], input1[3])
            elif i[1] == "AUTHOR_BOOK":
                View.display('author_id/book_id')
                input1 = View.input_many()
                Model.add_author_book_pair(input1[0], input1[1])
            elif i[1] == "PURCHASE_BOOK":
                View.display('purchase_id/book_id')
                input1 = View.input_many()
                Model.add_purchase_book_pair(input1[0], input1[1])
        elif i[0] == 'UPDATE':
            View.display('Updating...')
            if i[1] == "AUTHOR":
                View.display('author_id/author_name')
                input1 = View.input_many()
                View.display(input1)
                Model.update_author(input1[0], input1[1])
            elif i[1] == "BOOK":
                View.display('book_id/book_name/page_count/book_price')
                input1 = View.input_many()
                Model.update_book(input1[0], input1[1], input1[2], input1[3])
            elif i[1] == "PURCHASE":
                View.display('purchase_id/client_id/sum/transaction_number')
                input1 = View.input_many()
                Model.update_purchase(input1[0], input1[1], input1[2], input1[3])
            elif i[1] == "CLIENT":
                View.display('client_id/name/login/email')
                input1 = View.input_many()
                Model.update_client(input1[0], input1[1], input1[2], input1[3])
        elif i[0] == 'DELETE':
            View.display('Deleting...')
            if i[1] == "AUTHOR":
                Model.delete_author(int(i[2]))
            elif i[1] == "BOOK":
                Model.delete_book(int(i[2]))
            elif i[1] == "PURCHASE":
                Model.delete_purchase(int(i[2]))
            elif i[1] == "CLIENT":
                Model.delete_client(int(i[2]))
            elif  i[1] == "PURCHASE_BOOK":
                Model.delete_purchase_book_pairs_by_purchase_id(int(i[2]))
            elif  i[1] == "AUTHOR_BOOK":
                Model.delete_author_book_pairs_by_book_id(int(i[2]))
        elif i[0] == "GENERATE":
            View.display("Generating...")
            if i[1] == "AUTHORS":
                Model.add_random_authors(int(i[2]))
            elif i[1] == "BOOKS":
                Model.add_random_books(int(i[2]))
            elif i[1] == "PURCHASES":
                Model.add_random_purchases(int(i[2]))
            elif i[1] == "CLIENTS":
                Model.add_random_clients(int(i[2]))
            elif i[1] == "AUTHOR_BOOK_PAIRS":
                Model.add_random_author_book_pairs(int(i[2]))
            elif i[1] == "PURCHASE_BOOK_PAIRS":
                Model.add_random_purchase_book_pairs(int(i[2]))
        elif i[0] == 'SEARCH':
            View.display('Searching...')
            if i[1] == "CLIENT":
                result = Model.search_client(i[2])
                View.display(result)
            elif i[1] == "AUTHOR":
                result = Model.search_author(i[2])
                View.display(result)
            elif i[1] == "PURCHASE":
                result = Model.search_purchase(i[2])
                View.display(result)
            elif i[1] == "BOOK":
                if len(i) == 3:
                    result = Model.search_book_by_name(i[2])
                elif len(i) == 4:
                    result = Model.search_book(int(i[2]), int(i[3]))
                View.display_books1(result)
