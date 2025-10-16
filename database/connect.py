from psycopg2 import connect
from environs import Env

env = Env()
env.read_env()

def get_connect():
    return connect(
        user = env.str("USER"),
        password = env.str("PASSWORD"),
        host = env.str("HOST"),
        port = env.str("PORT"),
        database = env.str("DATABASE")
    )


def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS users (
        id BIGSERIAL PRIMARY KEY,
        fullname VARCHAR(200) NOT NULL,
        phone VARCHAR(50) UNIQUE NOT NULL,
        address TEXT NOT NULL,
        chat_id BIGINT UNIQUE NOT NULL,
        gender Varchar(50) NOT NULL,
        is_admin BOOLEAN DEFAULT FALSE,
        is_block BOOLEAN DEFAULT FALSE
    );

    CREATE TABLE IF NOT EXISTS category (
        id BIGSERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        is_active BOOLEAN DEFAULT TRUE
    );

    CREATE TABLE IF NOT EXISTS product (
        id BIGSERIAL PRIMARY KEY,
        name VARCHAR(200) NOT NULL,
        image TEXT NOT NULL,
        price BIGINT NOT NULL,
        quantity BIGINT NOT NULL,
        size VARCHAR(50) NOT NULL,
        season VARCHAR(20) NOT NULL,
        gender_type VARCHAR(20) NOT NULL,
        brand VARCHAR(50) NOT NULL,
        category_id BIGINT NOT NULL REFERENCES category(id)
    );

    CREATE TABLE IF NOT EXISTS orders (
        id BIGSERIAL PRIMARY KEY,
        chat_id BIGINT NOT NULL REFERENCES users(chat_id),
        product_id BIGINT NOT NULL REFERENCES product(id),
        price BIGINT NOT NULL,
        quantity BIGINT NOT NULL,
        status VARCHAR(50) NOT NULL DEFAULT 'new'
    );
    """
    with get_connect() as db:
        with db.cursor() as dbc:
            dbc.execute(sql)
            db.commit()
create_table()


