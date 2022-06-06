# sort by name
import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="206045",
    database="mydatabase"
)

my_cursor = my_db.cursor()

sort_by_name = "SELECT * FROM employees ORDER BY name"

my_cursor.execute(sort_by_name)

result = my_cursor.fetchall()

for i in result:
    print(i)


#-----------------------


import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="206045",
    database="mydatabase"
)

my_cursor = my_db.cursor()

sort_by_name = "SELECT * FROM employees ORDER BY name DESC"

my_cursor.execute(sort_by_name)

result = my_cursor.fetchall()

for i in result:
    print(i)
