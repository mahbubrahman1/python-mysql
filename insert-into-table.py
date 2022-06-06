import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="206045",
    database="students"
)

my_cursor = my_db.cursor()

ins = "INSERT INTO information (id, name, department) VALUES (%s, %s, %s)"
val = (95, "Mahbub", "CSE")

my_cursor.execute(ins, val)

my_db.commit()

print("record inserted successfully..")


#--------------------------


import mysql.connector

my_db = mysql.connector.connect(
	host="localhost",
	user="root",
	password="206045",
	database="mydatabase"
)

my_cursor = my_db.cursor()

# create employess table
# my_cursor.execute("CREATE TABLE employees (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), address VARCHAR(50))")

# insert the data into to the table

insert = "INSERT INTO employees(name, address) VALUES (%s, %s)"
value = ("John David", "Toronto, Canada")

my_cursor.execute(insert, value)

my_db.commit()

print("data insert successfully...")


#--------------------------


# insert multiple rows
import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="206045",
    database="mydatabase"
)

my_cursor = my_db.cursor()

insert = "INSERT INTO employees (name, address) VALUES (%s, %s)"
value = [
    ("Smith", "Lund, Sweden"),
    ("Maile", "Tokyo, Japan"),
    ("Jeimy", "Vancouver, Canada"),
    ("Bell", "Shenzhen, China"),
    ("Reyhan", "Dhaka, Bangladesh"),
    ("Carolina", "Seoul, South Korea"),
    ("Milton", "Los Angeles, US"),
]

my_cursor.executemany(insert, value)

my_db.commit()

print(my_cursor.rowcount, "was inserted successfully.")


#--------------------------


# insert into the table using user input
import mysql.connector

myDatabase = mysql.connector.connect(
	host="localhost",
	user="root",
	password="206045",
	database="myfirstdatabase"
)

myCursor = myDatabase.cursor()

student_name = input("Enter Student Name: ")
student_id = int(input("Enter ID: "))
department = input("Enter Department: ")
shift = input("Enter Shift: ")

insert = "INSERT INTO students VALUES ('{}', {}, '{}', '{}')".format(student_name, student_id, department, shift)

myCursor.execute(insert)

myDatabase.commit()

print("Data inserted successfully.")


#--------------------------


myDatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="206045",
    database="myfirstdatabase"
)

myCursor = myDatabase.cursor()

while True:
    student_name = input("Enter Student Name: ")
    student_id = int(input("Enter ID: "))
    department = input("Enter Department: ")
    shift = input("Enter Shift: ")

    insert = "INSERT INTO students VALUES ('{}', {}, '{}', '{}')".format(
        student_name, student_id, department, shift)

    myCursor.execute(insert)

    myDatabase.commit()

    print("Data inserted successfully.")

    decision = int(input("1. Insert More \n2. Exit \nChoose anyone: "))
    if decision == 2:
        break
