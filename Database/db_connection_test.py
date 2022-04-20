"""
Test the db connectivity

Dependency: 
https://pypi.org/project/mysql-connector-python/
pip install mysql-connector-python
Ref: https://www.w3schools.com/python/python_mysql_getstarted.asp
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="REPLACE_WITH_RDS_END_POINT",
  user="admin",
  password="Admin12345"
)

print(mydb)