from .connect import get_connect



def is_register_by_id(chat_id):
    try:
        with get_connect() as db:
            with db.cursor() as dbc:
                dbc.execute("select * from users where chat_id = %s",(chat_id,))
                return dbc.fetchone()
    except Exception as err:
        print(f"Register: {err}")
        return None
    

def is_admin_by_id(chat_id):
    try:
        with get_connect() as db:
            with db.cursor() as dbc:
                dbc.execute("select * from users where chat_id = %s and is_admin=true",(chat_id,))
                return dbc.fetchone()
    except Exception as err:
        print(f"Register: {err}")
        return None
    

def get_category():
    try:
        with get_connect() as db:
            dbc = db.cursor()
            dbc.execute("SELECT id, name FROM category WHERE is_active = true")
            categories = dbc.fetchall()
            dbc.close()
            return categories
    except Exception as err:
        print(f"Get Category error: {err}")
        return None

