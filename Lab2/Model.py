import psycopg2
import Controller

def add_author(author_id, author_name):
    conn, cur = Controller.connect()
    try:
        cur.execute("INSERT INTO \"Author\" (\"AuthorID\", \"Name\") VALUES (%s, %s)", (author_id, author_name))
    except:
        print("Can't add author.")
    conn.commit()
    cur.close()
    conn.close()

def get_author(author_id):
    conn, cur = Controller.connect()
    try:
        cur.execute("SELECT \"AuthorID\",\"Name\" FROM \"Author\" WHERE \"AuthorID\"='%s'", (author_id,))
    except:
        print("Can't get author.")
    return cur.fetchall()

def update_author(author_id, author_name):
    conn, cur = Controller.connect()
    try:
        cur.execute("UPDATE \"Author\" SET \"Name\"=%s WHERE \"AuthorID\"=%s", (author_name, author_id))
    except:
        print("Can't update author.")
    conn.commit()
    cur.close()
    conn.close()

def delete_author(author_id):
    conn, cur = Controller.connect()
    try:
        cur.execute("DELETE FROM \"Author\" WHERE \"AuthorID\"='%s'", (author_id,))
    except:
        print("Can't delete author.")
    conn.commit()
    cur.close()
    conn.close()


def add_book(book_id, book_name, page_count, book_price):
    conn, cur = Controller.connect()
    try:
        cur.execute("INSERT INTO \"Book\" (\"BookID\", \"Name\", \"PageCount\", \"Price\") VALUES (%s, %s, %s, %s);", (book_id, book_name, page_count, book_price))
    except:
        print("Can't add book.")
    conn.commit()
    cur.close()
    conn.close()

def get_book(book_id):
    conn, cur = Controller.connect()
    try:
        cur.execute("SELECT \"BookID\",\"Name\",\"PageCount\",\"Price\" FROM \"Book\" WHERE \"BookID\"='%s'", (book_id,))
    except:
        print("Can't get book.")
    return cur.fetchall()

def update_book(book_id, book_name, page_count, book_price):
    conn, cur = Controller.connect()
    try:
        cur.execute("UPDATE \"Book\" SET \"Name\"=%s, \"PageCount\"=%s, \"Price\"=%s WHERE \"BookID\"=%s", (book_name, page_count, book_price, book_id))
    except:
        print("Can't update book.")
    conn.commit()
    cur.close()
    conn.close()

def delete_book(book_id):
    conn, cur = Controller.connect()
    try:
        cur.execute("DELETE FROM \"Book\" WHERE \"BookID\"='%s'", (book_id,))
    except:
        print("Can't delete book.")
    conn.commit()
    cur.close()
    conn.close()

def add_author_book_pair(author_id, book_id):
    conn, cur = Controller.connect()
    try:
        cur.execute("INSERT INTO \"Author_Book\" (\"AuthorID\", \"BookID\") VALUES (%s, %s)", (author_id, book_id))
    except:
        print("Can't add author book pair.")
    conn.commit()
    cur.close()
    conn.close()

def get_authors_by_book_id(book_id):
    conn, cur = Controller.connect()
    try:
        cur.execute("SELECT \"AuthorID\" FROM \"Author_Book\" WHERE \"BookID\"='%s'", (book_id,))
    except:
        print("Can't get authors by book id.")
    return cur.fetchall()

def delete_author_book_pairs_by_book_id(book_id):
    conn, cur = Controller.connect()
    try:
        cur.execute("DELETE FROM \"Author_Book\" WHERE \"BookID\"='%s'", (book_id,))
    except:
        print("Can't delete author_book pair.")
    conn.commit()
    cur.close()
    conn.close()

def add_purchase_book_pair(purchase_id, book_id):
    conn, cur = Controller.connect()
    try:
        cur.execute("INSERT INTO \"Purchase_Book\" (\"PurchaseID\", \"BookID\") VALUES (%s, %s)", (purchase_id, book_id))
    except:
        print("Can't add purchase book pair.")
    conn.commit()
    cur.close()
    conn.close()

def get_books_by_purchase_id(purchase_id):
    conn, cur = Controller.connect()
    try:
        cur.execute("SELECT \"BookID\" FROM \"Purchase_Book\" WHERE \"PurchaseID\"='%s'", (purchase_id,))
    except:
        print("Can't get books by purchase id.")
    return cur.fetchall()

def delete_purchase_book_pairs_by_purchase_id(purchase_id):
    conn, cur = Controller.connect()
    try:
        cur.execute("DELETE FROM \"Purchase_Book\" WHERE \"PurchaseID\"='%s'", (purchase_id,))
    except:
        print("Can't delete purchase_book pair.")
    conn.commit()
    cur.close()
    conn.close()

def add_purchase(purchase_id, client_id, sum, transaction_number):
    conn, cur = Controller.connect()
    try:
        cur.execute("INSERT INTO \"Purchase\" (\"ClientID\", \"Sum\", \"BankTransactionNumber\", \"PurchaseID\") VALUES (%s, %s, %s, %s);", (client_id, sum, transaction_number, purchase_id))
    except:
        print("Can't add purchase.")
    conn.commit()
    cur.close()
    conn.close()

def get_purchase(purchase_id):
    conn, cur = Controller.connect()
    try:
        cur.execute("SELECT \"ClientID\", \"Sum\", \"BankTransactionNumber\", \"PurchaseID\" FROM \"Purchase\" WHERE \"PurchaseID\"='%s'", (purchase_id,))
    except:
        print("Can't get purchase")
    return cur.fetchall()

def update_purchase(purchase_id, client_id, sum, transaction_number):
    conn, cur = Controller.connect()
    try:
        cur.execute("UPDATE \"Purchase\" SET \"ClientID\"=%s, \"Sum\"=%s, \"BankTransactionNumber\"=%s WHERE \"PurchaseID\"=%s", (client_id, sum, transaction_number, purchase_id))
    except:
        print("Can't update purchase.")
    conn.commit()
    cur.close()
    conn.close()

def delete_purchase(purchase_id):
    conn, cur = Controller.connect()
    try:
        cur.execute("DELETE FROM \"Purchase\" WHERE \"PurchaseID\"='%s'", (purchase_id,))
    except:
        print("Can't delete purchase.")
    conn.commit()
    cur.close()
    conn.close()

def add_client(client_id, name, login, email):
    conn, cur = Controller.connect()
    try:
        cur.execute("INSERT INTO \"Client\" (\"ClientID\", \"Name\", \"Login\", \"Email\") VALUES (%s, %s, %s, %s);", (client_id, name, login, email))
    except:
        print("Can't add client.")
    conn.commit()
    cur.close()
    conn.close()

def get_client(client_id):
    conn, cur = Controller.connect()
    try:
        cur.execute("SELECT \"ClientID\", \"Name\", \"Login\", \"Email\" FROM \"Client\" WHERE \"ClientID\"='%s'", (client_id,))
    except:
        print("Can't get client.")
    return cur.fetchall()

def update_client(client_id, name, login, email):
    conn, cur = Controller.connect()
    try:
        cur.execute("UPDATE \"Client\" SET \"Name\"=%s, \"Login\"=%s, \"Email\"=%s WHERE \"ClientID\"=%s", (name, login, email, client_id))
    except:
        print("Can't update client.")
    conn.commit()
    cur.close()
    conn.close()

def delete_client(client_id):
    conn, cur = Controller.connect()
    try:
        cur.execute("DELETE FROM \"Client\" WHERE \"ClientID\"='%s'", (client_id,))
    except:
        print("Can't delete client.")
    conn.commit()
    cur.close()
    conn.close()

def add_random_authors(n):
    conn, cur = Controller.connect()
    for i in range(0, n):
        try:
            cur.execute("""INSERT INTO "Author"(\"AuthorID\", \"Name\")
                VALUES(
                    (random() * 99999999)::int,
                    (SELECT (chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii(' ')) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int)
                            )));""")
        except:
            i = i - 1
    conn.commit()
    cur.close()
    conn.close()

def add_random_books(n):
    conn, cur = Controller.connect()
    for i in range(0, n):
        try:
            cur.execute("""INSERT INTO "Book"(\"BookID\", \"Name\", \"PageCount\", \"Price\")
                    VALUES(
                        (random() * 99999999)::int,
                    (SELECT (chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int) ||
                            chr(ascii('B') + (random() * 25)::int)
                            )),
                            (random() * 999)::int,
                            (random() * 250)::int
                    )""")
        except:
            i = i - 1
    conn.commit()
    cur.close()
    conn.close()

#purchase_id, client_id, sum, transaction_number
def add_random_purchases(n):
    conn, cur = Controller.connect()
    for i in range(0, n):
        cur.execute("""INSERT INTO \"Purchase\" (\"PurchaseID\", \"ClientID\", \"Sum\", \"BankTransactionNumber\")
                    VALUES(
                        (random() * 99999999)::int,
                        (SELECT \"ClientID\" FROM \"Client\" ORDER BY RANDOM() LIMIT 1),
                        (random() * 2500)::int,
                        (SELECT (chr(ascii('U')) ||
                        chr(ascii('A')) ||
                        chr(ascii('0') + (random() * 9)::int) ||
                        chr(ascii('0') + (random() * 9)::int) ||
                        chr(ascii('0') + (random() * 9)::int) ||
                        chr(ascii('0') + (random() * 9)::int) ||
                        chr(ascii('0') + (random() * 9)::int) ||
                        chr(ascii('0') + (random() * 9)::int) ||
                        chr(ascii('0') + (random() * 9)::int) ||
                        chr(ascii('0') + (random() * 9)::int))))""")
    conn.commit()
    cur.close()
    conn.close()

#client_id, name, login, email
def add_random_clients(n):
    conn, cur = Controller.connect()
    for i in range(0, n):
        cur.execute("""INSERT INTO \"Client\" (\"ClientID\", \"Name\", \"Login\", \"Email\")
                 VALUES(
                    (random() * 999999999)::int,
                        (SELECT (chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii(' ') ) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int))),
                        (SELECT (chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int))),
                        (SELECT (chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('B') + (random() * 25)::int) ||
                        chr(ascii('@')) ||
                        chr(ascii('g')) ||
                        chr(ascii('m')) ||
                        chr(ascii('a')) ||
                        chr(ascii('i')) ||
                        chr(ascii('l')) ||
                        chr(ascii('.')) ||
                        chr(ascii('c')) ||
                        chr(ascii('o')) ||
                        chr(ascii('m')))))""")
    conn.commit()
    cur.close()
    conn.close()

def add_random_author_book_pairs(n):
    conn, cur = Controller.connect()
    for i in range(0, n):
        try:
            cur.execute("""INSERT INTO "Author_Book"(\"AuthorID\", \"BookID\")
                    VALUES(
                        (SELECT \"AuthorID\" FROM \"Author\" ORDER BY RANDOM() LIMIT 1),
                        (SELECT \"BookID\" FROM \"Book\" ORDER BY RANDOM() LIMIT 1)
                    )""")
        except:
            i = i - 1
    conn.commit()
    cur.close()
    conn.close()

def add_random_purchase_book_pairs(n):
    conn, cur = Controller.connect()
    for i in range(0, n):
        try:
            cur.execute("""INSERT INTO "Purchase_Book"(\"PurchaseID\", \"BookID\")
                    VALUES(
                        (SELECT \"PurchaseID\" FROM \"Purchase\" ORDER BY RANDOM() LIMIT 1),
                        (SELECT \"BookID\" FROM \"Book\" ORDER BY RANDOM() LIMIT 1)
                    )""")
        except:
            i = i - 1
    conn.commit()
    cur.close()
    conn.close()

def search_client(name):
    conn, cur = Controller.connect()
    s = "SELECT * FROM \"Client\" WHERE UPPER(\"Name\") LIKE '%" + name + "%' OR UPPER(\"Login\") LIKE '%" + name + "%' OR UPPER(\"Email\") LIKE '%" + name + "%' ;"
    print(s)
    try:
        cur.execute(s)
    except:
        print("Can't search book.")
    return cur.fetchall()

def search_author(name):
    conn, cur = Controller.connect()
    s = "SELECT * FROM \"Author\" WHERE UPPER(\"Name\") LIKE '%" + name + "%';"
    print(s)
    try:
        cur.execute(s)
    except:
        print("Can't search book.")
    return cur.fetchall()

def search_purchase(name):
    conn, cur = Controller.connect()
    s = "SELECT * FROM \"Purchase\" WHERE UPPER(\"BankTransactionNumber\") LIKE '%" + name + "%';"
    print(s)
    try:
        cur.execute(s)
    except:
        print("Can't search book.")
    return cur.fetchall()

def search_book(price_min, price_max):
    conn, cur = Controller.connect()
    try:
        cur.execute("SELECT * FROM \"Book\" WHERE %s <= (\"Price\"::numeric::int) and (\"Price\"::numeric::int) <= %s OR %s <= \"PageCount\" and \"PageCount\" <= %s OR %s <= \"BookID\" and \"BookID\" <= %s;", (price_min, price_max, price_min, price_max, price_min, price_max))
    except:
        print("Can't search book.")
    return cur.fetchall()

def search_book_by_name(name):
    conn, cur = Controller.connect()
    s = "SELECT * FROM \"Book\" WHERE UPPER(\"Name\") LIKE '%" + name + "%';"
    print(s)
    try:
        cur.execute(s)
    except:
        print("Can't search book.")
    return cur.fetchall()