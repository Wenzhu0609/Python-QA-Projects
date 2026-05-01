import mysql.connector
from mysql.connector import Error

from Python_QA_Framework.utilities.config import get_config, get_mysql_credentials


def get_mysql_connection():
    try:
        user, password = get_mysql_credentials()
        connect_config = {
            "host": get_config()["SQL"]["host"],
            "database": get_config()["SQL"]["database"],
            "user": user,
            "password": password,
        }

        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connection Successful!")
            return conn
    except Error as e:
        print(e)


# To connect to MySQL, run a query, and fetch one result row for use:
def get_query(query):
    conn = get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row


def fetch_one(query, data=None):
    conn = get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute(query, data)
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row


def fetch_all(query, data=None):
    conn = get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute(query, data)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def execute_query(query, data=None):
    conn = get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute(query, data)
    conn.commit()
    cursor.close()
    conn.close()
