import mysql.connector

myDatabase = mysql.connector.connect(
	host="localhost",
	user="root",
	password="206045",
	database="students"
)

myCursor = myDatabase.cursor()

deleteTable = "DROP TABLE information"

myCursor.execute(deleteTable)

print("deleted..!")