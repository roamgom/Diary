from DiaryClass import Diary
from pathlib import Path

import os.path


def DiaryMenu():
    print("""Welcome to Your Diary!

    ======MENU======
    1. Make New Diary
    2. Load Diary
    3. Exit\n""")
    select = int(input(">> "))

    if select is 1:
        NewUser()
    elif select is 2:
        check = FindUser()
        if check is True:
            UserMenu()
        else:
            print("No User!")
            return
    elif select is 3:
        return False
    else:
        return


def NewUser():
    print("""=====New Account=====
    Tell me your name!
    """)
    user_name = input(">> ")
    user = Diary(user_name)
    return


def FindUser():
    print("What's your name?")
    check_name = input(">> ")
    check_name.replace(" ", "_")
    check_filename = Path("./" + check_name + ".text")
    if check_filename.is_file():
        return True
    else:
        return False


def UserMenu():
    print("Welcome ", )

while True:
    DiaryMenu()