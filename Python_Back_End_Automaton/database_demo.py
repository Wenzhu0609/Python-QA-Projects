import mysql.connector
from utilities.configurations import get_mysql_credentials
# To connect to my database - hardcoded way: 
# Required fields: host, database, user, password
user, password = get_mysql_credentials()
conn = mysql.connector.connect(
    host='localhost', 
    database='PythonAutomation', 
    user=user, 
    password=password
    )
print(conn.is_connected())

cursor = conn.cursor()
cursor.execute("select * from CustomerInfo")
row = cursor.fetchone()           # Fetches the first row of the table
print(row)
print(row[3])
row = cursor.fetchone()         # Repeating  will cause it to fetch the next row, instead of the same one
print(row)
rowAll = cursor.fetchall()      # Fetches the remaining, not from the very begining
print(rowAll)               # lIst of tuples


conn.close