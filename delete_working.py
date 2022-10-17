import mysql.connector

# Get the SQL connection
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


def delete_fun(self):
    doctor_id=input("Enter the id : ")

    try:
        
        connection=get_connection()
        cursor=connection.cursor()
        sql_query="SELECT * FROM Doctor WHERE doctor_id= %s"
        cursor.execute(sql_query,(doctor_id,))
        records=cursor.fetchone()
        close_connection(connection)

        print("Data fetched: ", doctor_id)
        print("-----------------------------------------")
        print('Doctor_ID\t\t Doctor_Name')
        print('-------------------------------------------')       
        print(' {}\t\t\t {} '.format(records[0], records[1]))
        print('-------------------------------------------')


        confirm=input("Are you sure want to delete it (Y/N) ? ")
        
        if confirm == 'Y':
            
            connection=get_connection()
            cursor=connection.cursor()
            select_query = """DELETE from Doctor where Doctor_Id = %s"""
            cursor.execute(select_query, (doctor_id,))
            records=cursor.fetchall()
            close_connection(connection)
            print('Data deleted successfully!')
        else:
            print('Wrong Entry')                

    except:
        print("Please check, something went wrong")
    finally:
            connection.close()

    # except (Exception, mysql.connector.Error) as error:
    #     print("error")


delete_fun(101)

