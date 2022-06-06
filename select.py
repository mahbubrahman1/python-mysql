import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="206045",
    database="mydatabase"
)

my_cursor = my_db.cursor()

my_cursor.execute("SELECT * FROM employees")

result = my_cursor.fetchall()

for i in result:
    print(i)

#--------------------------


[NOTE: Sublime Text Editor a jodi ei code run korar khetre error dey tahole Python IDLE te new file ekta niye tarpor code bosiye save kore run kore dekho. thikthakmoto kaj korbe]

#--------------------------

import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="206045",
    database="mydatabase"
)

my_cursor = my_db.cursor()

my_cursor.execute("SELECT name, address FROM employees")

result = my_cursor.fetchall()

for i in result:
    print(i)


#--------------------------


import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="206045",
    database="mydatabase"
)

my_cursor = my_db.cursor()

my_cursor.execute("SELECT name FROM employees")

result = my_cursor.fetchall()

for i in result:
    print(i)


#--------------------------


# If you are only interested in one row, you can use the fetchone() method.
import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="206045",
    database="mydatabase"
)

my_cursor = my_db.cursor()

my_cursor.execute("SELECT name, address FROM employees")

result = my_cursor.fetchone()

for i in result:
    print(i)