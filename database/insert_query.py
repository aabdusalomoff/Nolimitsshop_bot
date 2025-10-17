from .connect import get_connect

def insert_user(fullname, phone, gender, address, chat_id):
    try:
        with get_connect() as db:
            with db.cursor() as dbc:

                dbc.execute("insert into users(fullname, phone, gender, address, chat_id) " \
                "values(%s,%s,%s,%s,%s)",(fullname,phone,gender,address,chat_id))

                db.commit()
                return True
    except Exception as err:

        print(f"User save: {err}")
        return None 