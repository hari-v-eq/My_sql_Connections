import mysql.connector


def get_connection():
    connection=mysql.connector.connect(
        host="localhost",
        database="python_db",
        port=3307,
        username="root",
        password="")

    return connection

def close_connection(connection):
    if connection:
        connection.close()


def insert_to(hospital_id,hospital_name,bed_count):
    try:
        connection=get_connection()
        cursor=connection.cursor()
        
        insert_query="insert into hospital (Hospital_Id,Hospital_Name,Bed_Count) values (%s,%s,%s)"
        cursor.execute(insert_query,(hospital_id,hospital_name,bed_count,))
        records=cursor.fetchall()
        connection.commit()
        close_connection(connection)
    
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)


print("Data has been Updated ")
insert_to(6,"ABC hospital",2000)