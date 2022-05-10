"""
To read data from the table
"""

import mysql.connector
import utils

mydb = mysql.connector.connect(
    host=utils.DB_HOST,
    user=utils.DB_USER_NAME,
    password=utils.DB_PASSWORD,
    database=utils.DB_NAME
)

mycursor = mydb.cursor()

# select all rows and columns from the table
# mycursor.execute("SELECT * FROM customers")

# if we want specific columns instead of all columns in the table
# mycursor.execute("SELECT name FROM customers")

# if we want specific row based on the condition
mycursor.execute("SELECT * FROM customers where Name='Vicky'") 

myresult = mycursor.fetchall()

for x in myresult:
  print(x)