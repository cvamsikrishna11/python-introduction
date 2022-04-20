"""
Create a new table in the testdb
"""

import mysql.connector
import utils

mydb = mysql.connector.connect(
  host=utils.DB_HOST,
  user=utils.DB_USER_NAME,
  password=utils.DB_PASSWORD,
  database = utils.DB_NAME
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)