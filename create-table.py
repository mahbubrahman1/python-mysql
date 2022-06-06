import mysql.connector

my_db = mysql.connector.connect(
	host="localhost",
	user="root",
	password="206045",
	database="students"
)

my_cursor = my_db.cursor()


# Create Table
# my_cursor.execute("CREATE TABLE information (id INT PRIMARY KEY, name VARCHAR(80), department VARCHAR(80))")


# Show Table
my_cursor.execute("SHOW TABLES")

for i in my_cursor:
	print(i)

# evabe ekta kore dekhabe. jodi bhalo kore dekhte cao tahole MySQL shall a giye database change kore (show tables;) commend likho.