from .connect import get_connect
import logging

logger = logging.getLogger(__name__)

def insert_user(fullname, phone, gender, address, chat_id):
    try:
        with get_connect() as db:
            dbc = db.cursor()
            sql = """
            INSERT INTO users (fullname, phone, gender, address, chat_id)
            VALUES (?, ?, ?, ?, ?)
            """
            dbc.execute(sql, (fullname, phone, gender, address, chat_id))
            db.commit()
            logger.info(f"User {chat_id} saved to database")
            return True

    except Exception as err:
        logger.error(f"User save error for {chat_id}: {err}")
        return False
