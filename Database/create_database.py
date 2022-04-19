"""
To create an empty database for our works

Ref: https://www.w3schools.com/python/python_mysql_create_db.asp
"""

import mysql.connector
import utils

mydb = mysql.connector.connect(
  host=utils.DB_HOST,
  user=utils.DB_USER_NAME,
  password=utils.DB_PASSWORD
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE testdb")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
