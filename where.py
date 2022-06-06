import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="206045",
    database="mydatabase"
)

my_cursor = my_db.cursor()

filtering = "SELECT * FROM employees WHERE address='Vancouver, Canada'"

my_cursor.execute(filtering)

result = my_cursor.fetchall()

for i in result:
    print(i)

# aro vivinnota deowa ache w3schools website a