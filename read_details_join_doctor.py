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

def read_fun():
    hospital_id=input("Enter the Hospital id: ")
    try: 
        connection=get_connection()
        cursor=connection.cursor()
        sql2_query="SELECT doctor.Doctor_Id, doctor.Doctor_Name, hospital.Hospital_Name FROM doctor INNER JOIN hospital ON doctor.hospital_id=hospital.hospital_id where hospital.hospital_id= %s"
        cursor.execute(sql2_query,(hospital_id,))
        records=cursor.fetchall()
        
        close_connection(connection)


        print("Data fetched: ", hospital_id,)

        print("-----------------------------------------")
        print('Doctor_ID     Doctor_Name   \tHospital_Name')
        print('-------------------------------------------')  

        for i in records:
                
            print("{}\t\t{}\t\t{}\t".format(i[0],i[1],i[2]))
        

       
    except:
        print("Please check, something went wrong")
    finally:
        connection.close()

read_fun()

