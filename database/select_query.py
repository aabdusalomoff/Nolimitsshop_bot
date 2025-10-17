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
    
