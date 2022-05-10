"""
To create an empty database for our works

Ref: https://www.w3schools.com/python/python_mysql_getstarted.asp

https://pypi.org/project/mysql-connector-python/
"""

import mysql.connector # install the pip dependency of mysql using https://pypi.org/project/mysql-connector-python/
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
# successfully created db