import mysql.connector

my_db = mysql.connector.connect(
	host="localhost",
	user="root",
	password="206045"
)

if my_db.is_connected():
	print("connected")

else:
	print("error")
	