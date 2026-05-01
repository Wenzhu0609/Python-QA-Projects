from Python_QA_Framework.utilities.db_utils import get_mysql_connection


conn = get_mysql_connection()
print(conn.is_connected())

cursor = conn.cursor()
cursor.execute("select * from CustomerInfo")
row = cursor.fetchone()           # Fetches the first row of the table
print(row)
print(row[3])
row = cursor.fetchone()         # Repeating  will cause it to fetch the next row, instead of the same one
print(row)
row_all = cursor.fetchall()      # Fetches the remaining, not from the very beginning
print(row_all)                   # list of tuples


cursor.close()
conn.close()
