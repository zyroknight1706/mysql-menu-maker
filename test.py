import mysql.connector as sql

lol = sql.connect(host='localhost', user='root', passwd='Zyros')
cur  = lol.cursor()

cur.execute('show databases;')

if 'anotherdb' in cur:
    print(True)
else:
    print(False)