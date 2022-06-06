import mysql.connector

myDatabase = mysql.connector.connect(
	host="localhost",
	user="root",
	password="206045",
	database="myfirstdatabase"
)

myCursor = myDatabase.cursor()

delete = "DELETE FROM students WHERE id=85"

myCursor.execute(delete)

myDatabase.commit()

print("Record deleted")