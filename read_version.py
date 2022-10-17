#Exercise 1: Connect to your database server and print its version

import mysql.connector

def get_connection():
    connection=mysql.connector.connect(
        host="localhost",
        port=3307,
        database="python_db",
        username="root",
        password="")
    

    return connection

def close_connection(connection):
    if connection:
        connection.close()


def read_db_version():
    try:
        connection=get_connection()
        cursor=connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("You are connected to MySQL version: ", db_version)
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)


print("Question 1: Print Database version")
read_db_version()