from logs import Logger
import sqlite3

logger = Logger().get_log()

class Connection():

    def __init__(self, db_name="expenses"):
        logger.info("Creating connection with db")
        try:
            self.conn = sqlite3.connect(db_name)
            self.conn.execute("PRAGMA foreign_keys = ON")
            self.cursor = self.conn.cursor()

            logger.info("Connection created successfully")

        except Exception as e:
            logger.error(f"Connection failed: {e}")
            raise

    def commit(self):
        self.conn.commit()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor
    
    def commit(self):
        self.conn.commit()