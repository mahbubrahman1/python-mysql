"""import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="206045",
    database="mydatabase"
)

my_cursor = my_db.cursor()

update_table = "UPDATE employees SET address = 'Trabzon, Turkey' WHERE address = 'Dhaka, Bangladesh'"

my_cursor.execute(filtering)

my_db.commit()

print("Records updated.")
"""


#---------------


"""import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="206045",
    database="mydatabase"
)

my_cursor = my_db.cursor()

update_table = "UPDATE employees SET name = 'Zhāng' WHERE name = 'Bell'"

my_cursor.execute(update_table)

my_db.commit()

print("Records updated.")"""



#---------------

import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="206045",
    database="mydatabase"
)

my_cursor = my_db.cursor()

update_table = "UPDATE employees SET address = %s WHERE address = %s"
value = ("Pune, India", "Vancouver, Canada")

my_cursor.execute(update_table, value)

my_db.commit()

print("Records updated.")