#MySQL backend functions to use
from logging import error
import mysql.connector as connect
import random
import pickle

conn = None
cur = None

#userfile = open('../user.dat', "wb")

def authorize(uname, passwd):
    '''gotta check whether you're the real guy or a just a filthy hacker!!'''
    #global variables for working throughout the whole backend_sql.py
    global conn, cur

    #things can really die if you don't take precaution while handling databases!!
    try:
        conn = connect.connect(host='localhost', user=uname, passwd=passwd)
    except error:
        print(error)
        return error
    
    #cursors to use while working
    cur = conn.cursor()

    #check for our database!
    cur.execute('show databases;')

    #if it is in there, then use it,
    #if not then make it with the tables!

    dat = cur.fetchall()

    if ('dishdatabase',) in dat:
        print('database exists!')
        print('accessing database...')

        cur.execute('use dishdatabase;')
        return 'successful'
    else:
        print('database doesn\'t exist\ncreating new database...')
    
        cur.execute('create database dishdatabase;')

        print('database creation successful!')

        print('adding the necessary tables...')

        print('accessing database...')
        cur.execute('use dishdatabase;')
        cur.execute('create table dishes(dishname varchar(64), dishtype varchar(16));')
        return 'successful'
#end of authorize


def AddDishInDatabase(dname, dtype):
    '''adding a dish!! EZ!!!'''
    #dish adding code in cursor
    cur.execute('insert into dishes values("'+dname+'", "'+dtype+'");')

    conn.commit()
    #obviously it's successful now
    #don't even know what this code does
    return 'successful'
#end of AddDishInDatabase


def randomizeDish(course, md):
    '''giving a random dish of the specific course to the user!!'''

    cur.execute('select * from dishes;')

    dish_list = list()

    #loop to pick all the dishes of the specified category
    for i in cur:
        if course in i:
            dish_list.append(i[0])
    #end of the picking loop

    #remove all the dishes that have been used already
    for i in md:
        if course in md[i]:
            dish_list.remove(md[i][course])
    #end of the removing loop

    return dish_list[random.randint(0, len(dish_list)-1)]
#end of randomizeDish