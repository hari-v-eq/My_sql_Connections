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



def delete_id(doctor_id): 

        try:
            connection=get_connection()
            cursor=connection.cursor()
            select_query = """DELETE from Doctor where Doctor_Id = %s"""
            cursor.execute(select_query, (doctor_id,))
            records=cursor.fetchall()
            connection.commit()
            print("Data deleted Successfully")
            close_connection(connection)

        except (Exception, mysql.connector.Error) as error:
            print("Error while getting doctor's data", error)

print("Enter to doctor_id delete: ")
delete_id(101)




