from Python_QA_Framework.utilities.db_utils import get_mysql_connection


conn = get_mysql_connection()

# To fetch from the database:
cursor = conn.cursor()
cursor.execute("select * from CustomerInfo")
rows = cursor.fetchall()
print(type(rows))
print(rows)

# Example of using data fetched from the database:
total = 0
for row in rows:
    total = total + row[2]
print(total)

# To make updates to the database:
query = "update CustomerInfo set Location = %s where CourseName = %s"
data = ("UK", "Jmeter")
cursor.execute(query,data)
conn.commit()

# To delete a dataset from the database:
query = "delete from customerInfo where courseName = 'WebServices'"
cursor.execute(query)
conn.commit()




cursor.close()
conn.close()
