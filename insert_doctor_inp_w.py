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

def insert_doctor():
    try:
        connection=get_connection()
        cursor=connection.cursor()
        
        doctor_id=input("Doctor_id: ")
        
        doctor_name=input("Doctor_name: ")
        
        hospital_id=input("Hospital_id: ")
        
        joining_date=input("Joining date: ")
        
        speciality=input("Speciality: ")
       
        salary=input("salary: ")
        
        experience=input("Experience: ")

        val=(doctor_id,doctor_name,hospital_id,joining_date,speciality,salary,experience)
        insert_query="INSERT INTO doctor (Doctor_Id,Doctor_Name,Hospital_Id,Joining_Date,Speciality,Salary,Experience) values (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(insert_query,val)
        connection.commit()
        print("Data updated Successfully")
        record = cursor.fetchall()        
        close_connection(connection)
        
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

print("enter the below data: ")
insert_doctor()




