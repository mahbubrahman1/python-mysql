import mysql.connector

my_db = mysql.connector.connect(
	host="localhost",
	user="root",
	password="206045"
)

my_cursor = my_db.cursor()

my_cursor.execute("SHOW DATABASES")

for i in my_cursor:
	print(i)