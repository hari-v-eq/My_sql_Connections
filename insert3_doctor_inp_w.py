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



def func_CreateData():   
            
    hospital_id = input('Enter id = ')
    hospital_name = input('Enter name = ')
    bed_count= input("Enter no of beds: ")

    try:
        
        connection=get_connection()
        cursor=connection.cursor()
        
        insert_query="insert into hospital (Hospital_Id,Hospital_Name,Bed_Count) values (%s,%s,%s)"
        cursor.execute(insert_query,(hospital_id,hospital_name,bed_count,))
        records=cursor.fetchall()
        connection.commit()
        print("Data updated Successfully")
        close_connection(connection)
    
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)




    #     connection=get_connection 
    #     query = "insert into hospital (Hospital_Id,Hospital_Name,Bed_Count) values (%s,%s,%s)" 
    #     cursor = connection.cursor()

    #     # Execute the sql query
    #     cursor.execute(query, [hospital_id,hospital_name,bed_count])

    #     # Commit the data
    #     connection.commit()
    #     close_connection(connection)
    #     print('Data Saved Successfully')

    # except:
    #         print('Something wrong, please check')

    # finally:
    #     # Close the connection
    #     connection.close()

print("Enter the following data: ")

func_CreateData()