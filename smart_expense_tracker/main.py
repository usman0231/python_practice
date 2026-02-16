from logs import Logger
from init import db_init
from query import Query

logger = Logger().get_log()

db_init()

run = True

query = Query()

while run:

    is_logged_in = query.get_isLogged_status()

    print(f"Logged in status: {is_logged_in}")

    if is_logged_in == False:
        print("1. Login \n 2. SingUp \n 3. Exit")
        opt = int(input())

        if opt == 1:
            print("Email:")
            email = input()
            print("Pass:")
            password = input()
            query.login(email, password)

        elif opt == 2:
            print("Name:")
            name = input()
            print("Email:")
            email = input()
            print("Pass:")
            password = input()
            query.create_user(name, email, password)

        elif opt == 3:
            run = False
            exit()
        else:
            print("Invalid option")

    if is_logged_in == True:
        print("1. Add Expense \n 2. View Expenses \n 3. Export Expenses \n 4. Logout")
        opt = int(input())

        if opt == 1:
            print("Amount:")
            amount = float(input())
            print("Description:")
            description = input()
            query.add_expense(amount, description)
        elif opt == 2:
            expenses = query.view_expenses()
            for expense in expenses:
                print(expense)
        elif opt == 3:
            query.export_expenses()
        elif opt == 4:
            query.is_logged_in = False
            query.__user_id = None
            logger.info("User logged out successfully")
        else:
            print("Invalid option")
        