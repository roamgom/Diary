from DiaryClass import Diary
from pathlib import Path

import os.path


username = ''

def DiaryMenu():
    while True:
        print("""Welcome to Your Diary!

======MENU======
1. Make New Diary
2. Load Diary
3. Exit\n""")
        select = int(input(">> "))

        if select is 1:
            NewUser()
            UserMenu()
        elif select is 2:
            check = FindUser()
            if check is True:
                UserMenu()
            else:
                print("No User!")
                return
        elif select is 3:
            break
        else:
            print("Wrong Input!")
            continue


def NewUser():
    print("""=====New Account=====
    Tell me your name!
    """)
    while True:
        user_name = input(">> ")
        user_name.replace(" ", "_")
        check_filename = Path("./" + user_name + ".text")
        if check_filename.is_file():            #Check if file exists
            print("The User Already Exists!")
            continue
        else:                                   #Make new file
            new_user = Diary(user_name)
            user_name.replace("_", " ")
            global username
            username = user_name
            print("User Created!\n", user_name)
            break
    return


def FindUser():
    print("What's your name?")
    check_name = input(">> ")
    check_name.replace(" ", "_")
    check_filename = Path("./" + check_name + ".text")
    if check_filename.is_file():
        check_name.replace("_", " ")
        print("User Found!\n")
        global username         #Set username for using menu
        username = check_name
        return True
    else:
        print("No User!")
        return False


def UserMenu():
    exist_user = Diary(username)

    while True:
        print("Welcome \'", username,"\'")
        print("""
======USER MENU======
1. Write Diary
2. Read Diary
3. Exit""")

        select = int(input(">> "))

        if select is 1:
            exist_user.write_diary()
            exist_user.save_diary()
        elif select is 2:
            exist_user.read_diary()
        elif select is 3:
            return
        else:
            print("Wrong Input!")
            continue

