#app.py for all the main app stuff, to compile it all in just one place
from distutils.log import error
import AppModes
import backend.backend_SQL as sql
import pickle

def AppInit():
    #initialization, authentication and database access
    while True:
            uname = input("Please enter the username: ")
            passwd = input('Please enter the MySQL password: ')
            res = sql.authorize(uname, passwd)
            if res == 'successful':
                print('authorization successful!')
                break
            else:
                print(res)
                continue

    print("Welcome to the menu-maker software!")
    while True:
        print('(1): Make a menu\n(2): add a dish\n(3): Exit the program')
        choice = input('what would you like to do?(1, 2 or 3): ')
        if choice == '1':
            choice2 = AppModes.MakeAMenuMode()
            if choice2 == 'exit':
                break
            else:
                continue
        elif choice == '2':
            choice2 = AppModes.AddADishMode()
            if choice2 == 'exit':
                break
            else:
                continue
        elif choice == '3':
            break
        else:
            print('wrong choice please try again!!')