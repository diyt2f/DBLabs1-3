from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Table, and_
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
import Controller

engine = create_engine('postgresql://postgres:qwe123@localhost:5432/Lab1BookShop', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

book_purchase = Table('Purchase_Book', Base.metadata,
    Column('PurchaseID', ForeignKey('Purchase.PurchaseID'), primary_key=True),
    Column('BookID', ForeignKey('Book.BookID'), primary_key=True),
)

book_author =  Table('Author_Book', Base.metadata,
    Column('AuthorID', ForeignKey('Author.AuthorID'), primary_key=True),
    Column('BookID', ForeignKey('Book.BookID'), primary_key=True)
)

class Author(Base):
    __tablename__ = 'Author'
    AuthorID = Column(Integer, primary_key=True)
    Name = Column(String)
    Books = relationship('Book', secondary=book_author, back_populates='Authors')
    def __init__(self, author_id, name):
        self.AuthorID = author_id
        self.Name = name

class Book(Base):
    __tablename__ = 'Book'
    BookID = Column(Integer, primary_key=True)
    Name = Column(String)
    PageCount = Column(Integer)
    Price = Column(Integer)
    Purchases = relationship('Purchase', secondary=book_purchase, back_populates='Books')
    Authors = relationship('Author', secondary=book_author, back_populates='Books')
    def __init__(self, book_id, name, page_count, price):
        self.BookID = book_id
        self.Name = name
        self.PageCount = page_count
        self.Price = price

class Client(Base):
    __tablename__ = 'Client'
    ClientID = Column(Integer, primary_key=True)
    Name = Column(String)
    Login = Column(String)
    Email = Column(String)
    Purchases = relationship('Purchase', backref='Clients')
    def __init__(self, client_id, name, login, email):
        self.ClientID = client_id
        self.Name = name
        self.Login = login
        self.Email = email

class Purchase(Base):
    __tablename__ = 'Purchase'
    PurchaseID = Column(Integer, primary_key=True)
    Sum = Column(Integer)
    ClientID = Column(Integer, ForeignKey('Client.ClientID'))
    BankTransactionNumber = Column(String)
    Books = relationship('Book', secondary=book_purchase, back_populates='Purchases')
    def __init__(self, purchase_id, client_id, sum, transaction_number):
        self.PurchaseID = purchase_id
        self.ClientID = client_id
        self.Sum = sum
        self.BankTransactionNumber = transaction_number

def connect():
    Base.metadata.create_all(engine)

def add_author(author_id, author_name):
    lib = Author(author_id, author_name)
    session.add(lib)
    session.commit()

def get_author(author_id):
    lib = session.query(Author).filter(Author.AuthorID == int(author_id)).first()
    r = [lib.AuthorID, lib.Name]
    return r

def update_author(author_id, author_name):
    lib = session.query(Author).filter(Author.AuthorID == int(author_id)).first()
    lib.Name = author_name
    session.commit()

def delete_author(author_id):
    lib = session.query(Author).filter(Author.AuthorID == int(author_id)).first()
    session.delete(lib)
    session.commit()


def add_book(book_id, book_name, page_count, book_price):
    lib = Book(book_id, book_name, page_count, book_price)
    session.add(lib)
    session.commit()

def get_book(book_id):
    lib = session.query(Book).filter(Book.BookID == int(book_id)).first()
    r = [lib.BookID, lib.Name, lib.PageCount, lib.Price]
    return r

def update_book(book_id, book_name, page_count, book_price):
    lib = session.query(Book).filter(Book.BookID == int(book_id)).first()
    lib.Name = book_name
    lib.PageCount = page_count
    lib.Price = book_price
    session.commit()

def delete_book(book_id):
    lib = session.query(Book).filter(Book.BookID == int(book_id)).first()
    session.delete(lib)
    session.commit()

def add_author_book_pair(author_id, book_id):
    lib = session.query(Author).filter(Author.AuthorID == int(author_id)).first()
    lib.Books.append(session.query(Book).filter(Book.BookID == int(book_id)).first())
    session.add(lib)
    session.commit()

def get_authors_by_book_id(book_id):
    lib = session.query(Author).join(book_author).join(Book).filter(Book.BookID == book_id).all()
    r = []
    for i in lib:
        r.append([i.AuthorID, i.Name])
    return r

def delete_author_book_pairs_by_book_id(book_id):
    lib = session.query(Author).join(book_author).join(Book).filter(Book.BookID == book_id).all()
    for i in lib:
        session.delete(i)
    session.commit()

def add_purchase_book_pair(purchase_id, book_id):
    lib = session.query(Purchase).filter(Purchase.PurchaseID == int(purchase_id)).first()
    lib.Books.append(session.query(Book).filter(Book.BookID == int(book_id)).first())
    session.add(lib)
    session.commit()

def get_books_by_purchase_id(purchase_id):
    lib = session.query(Book).join(book_purchase).join(Purchase).filter(Purchase.PurchaseID == purchase_id).all()
    r = []
    for i in lib:
        r.append([i.BookID, i.Name, i.PageCount, i.Price])
    return r

def delete_purchase_book_pairs_by_purchase_id(purchase_id):
    lib = session.query(Book).join(book_purchase).join(Purchase).filter(Purchase.PurchaseID == purchase_id).all()
    for i in lib:
        session.delete(i)
    session.commit()

def add_purchase(purchase_id, client_id, sum, transaction_number):
    lib = Purchase(purchase_id, client_id, sum, transaction_number)
    session.add(lib)
    session.commit()

def get_purchase(purchase_id):
    lib = session.query(Purchase).filter(Purchase.PurchaseID == int(purchase_id)).first()
    r = [lib.PurchaseID, lib.Sum, lib.BankTransactionNumber, lib.ClientID]
    return r

def update_purchase(purchase_id, client_id, sum, transaction_number):
    lib = session.query(Purchase).filter(Purchase.PurchaseID == int(purchase_id)).first()
    lib.ClientID = client_id
    lib.Sum = sum
    lib.BankTransactionNumber = transaction_number
    session.commit()

def delete_purchase(purchase_id):
    lib = session.query(Purchase).filter(Purchase.PurchaseID == int(purchase_id)).first()
    session.delete(lib)
    session.commit()

def add_client(client_id, name, login, email):
    lib = Client(client_id, name, login, email)
    session.add(lib)
    session.commit()

def get_client(client_id):
    lib = session.query(Client).filter(Client.ClientID == int(client_id)).first()
    r = [lib.ClientID, lib.Name, lib.Login, lib.Email]
    return r


def update_client(client_id, name, login, email):
    lib = session.query(Client).filter(Client.ClientID == int(client_id)).first()
    lib.Name = name
    lib.Login = login
    lib.Email = email
    session.commit()

def delete_client(client_id):
    lib = session.query(Client).filter(Client.ClientID == int(client_id)).first()
    session.delete(lib)
    session.commit()

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