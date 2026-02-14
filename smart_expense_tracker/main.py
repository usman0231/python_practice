from logs import Logger
from init import db_init

logger = Logger().get_log()

db_init()

run = True

while run:
    print("1. Login \n 2. SingUp")
    opt = int(input())

    if opt == 1:
        pass
    elif opt == 2:
        print("Name:")
        name = input()
        print("Email:")
        email = input()
        print("Pass:")
        password = input()
        