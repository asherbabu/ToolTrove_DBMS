#Database testing, not connected to the official project, Ignore

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "tiger",
    database = "ToolTrove"
)

my_cursor = mydb.cursor()

#my_cursor.execute("CREATE DATABASE tooltroveex")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)