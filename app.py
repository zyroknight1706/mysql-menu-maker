#app.py for all the main app stuff, to compile it all in just one place
import AppModes
import backend.backend_SQL as sql

def AppInit():
    #initialization, authentication and 
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
    print('(1): Make a menu\n(2): add a dish')
    choice = input('what would you like to do?(1 or 2): ')
    while True:
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
        else:
            print('wrong choice please try again!!')