import mysql.connector

def get_connection():
    connection=mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    port=3307,
    database='python_db')

    return connection

def close_connection(connection):
    if connection:
        connection.close()