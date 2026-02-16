from logs import Logger
from db import Connection
import time

logger = Logger().get_log()
db = Connection()

class Query:

    def __init__(self, user_id=None):
        self.is_logged_in = False
        self.__user_id = None

        if user_id:
            self.__user_id = user_id
            self.is_logged_in = True
        
    def get_isLogged_status(self):
        return self.is_logged_in

    def create_user(self, name, email, password):
        try:
            if self.is_logged_in:
                logger.warning("User creation failed: User already logged in")
                return
            db.execute("""
            INSERT INTO users (name, email, password) VALUES (?, ?, ?)
            """, (name, email, password))
            db.commit()
            logger.info("User created successfully")
        except Exception as e:
            logger.error(f"User creation failed: {e}")

    def get_user_by_email(self, email):
        try:
            db.execute("""
            SELECT * FROM users WHERE email = ?
            """, (email,))
            user = db.fetchone()
            return user
        except Exception as e:
            logger.error(f"User retrieval failed: {e}")
            return None
        
    def login(self, email, password):
        if self.is_logged_in:
            print("Already logged in")
            return
        
        user = self.get_user_by_email(email)
        print(user)
        if user and user[3] == password:
            print("Login successful")
            logger.info("Login successful")
            self.is_logged_in = True
            self.__user_id = user[0]
            return user
        else:
            logger.warning("Login failed: Invalid email or password")
            return None
        
    def add_expense(self, amount, description=""):
        try:
            if not self.is_logged_in:
                logger.warning("Expense addition failed: User not logged in")
                return
            user_id = self.__user_id
            db.execute("""
            INSERT INTO expense (user_id, amount, description) VALUES (?, ?, ?)
            """, (user_id, amount, description))
            db.commit()
            logger.info("Expense added successfully")
        except Exception as e:
            logger.error(f"Expense addition failed: {e}")

    def view_expenses(self):
        try:
            if not self.is_logged_in:
                logger.warning("Expense retrieval failed: User not logged in")
                return []
            
            user_id = self.__user_id

            db.execute("""
            SELECT amount, description, date FROM expense WHERE user_id = ?
            """, (user_id,))
            expenses = db.fetchall()
            return expenses
        except Exception as e:
            logger.error(f"Expense retrieval failed: {e}")
            return []
        
    def export_expenses(self):
        try:
            if not self.is_logged_in:
                logger.warning("Expense export failed: User not logged in")
                return
            
            db.execute("""
            SELECT users.name, users.email, expense.amount, expense.description, expense.date 
                       FROM expense 
                       INNER JOIN users ON expense.user_id = users.id
            """)
            expenses = db.fetchall()

            filename = "expenses_export" + time.strftime("%Y%m%d-%H%M%S") + ".csv"

            with open(filename, "w") as f:
                f.write("Amount,Description,Date\n")
                for expense in expenses:
                    f.write(f"{expense[0]},{expense[1]},{expense[2]}\n")
            logger.info("Expenses exported successfully")
        except Exception as e:
            logger.error(f"Expense export failed: {e}")