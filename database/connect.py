import sqlite3

def get_connect():
    return sqlite3.connect("shop.db")

def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT NOT NULL,
        phone TEXT UNIQUE NOT NULL,
        address TEXT NOT NULL,
        chat_id INTEGER UNIQUE NOT NULL,
        gender TEXT NOT NULL,
        is_admin BOOLEAN DEFAULT 0,
        is_block BOOLEAN DEFAULT 0
    );

    CREATE TABLE IF NOT EXISTS category (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        is_active BOOLEAN DEFAULT 1
    );

    CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        image TEXT NOT NULL,
        price INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        size TEXT NOT NULL,
        season TEXT NOT NULL,
        gender_type TEXT NOT NULL,
        brand TEXT NOT NULL,
        category_id INTEGER NOT NULL,
        FOREIGN KEY (category_id) REFERENCES category (id)
    );

    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        price INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        status TEXT NOT NULL DEFAULT 'new',
        FOREIGN KEY (chat_id) REFERENCES users (chat_id),
        FOREIGN KEY (product_id) REFERENCES product (id)
    );
    """
    with get_connect() as db:
        dbc = db.cursor()
        dbc.executescript(sql)
        db.commit()

create_table()
