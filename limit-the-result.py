import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="206045",
    database="mydatabase"
)

my_cursor = my_db.cursor()

my_cursor.execute("SELECT * FROM employees LIMIT 3")

result = my_cursor.fetchall()

for i in result:
    print(i)


#--------------------


# Start from position 3, and return 5 records
import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="206045",
    database="mydatabase"
)

my_cursor = my_db.cursor()

my_cursor.execute("SELECT * FROM employees LIMIT 3 OFFSET 2")

result = my_cursor.fetchall()

for i in result:
    print(i)
