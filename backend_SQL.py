#backend functions and useful variables for MySQL
#hope there aren't too many functions in here uwu
from logging import error
import mysql.connector as con

conn = None
#database connection

def authorized(username, passwd):
    global conn
    try:
        conn = con.connect(host='localhost', user=username, passwd=passwd)
    except error:
        print(error)
        return "Wrong username or password. Please try again!"
    
    #database connection check
    if conn.is_connected():
        print("database connected")
        return "ok"
cur = conn.cursor()