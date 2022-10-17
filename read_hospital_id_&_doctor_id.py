#Question 2: Fetch Hospital and Doctor Information using hospital Id and doctor Id


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

def get_hospital_details(hospital_id):
    try:
        connection=get_connection()
        cursor=connection.cursor()
        select_query="SELECT * FROM Hospital WHERE Hospital_Id = %s"
        cursor.execute(select_query,(hospital_id,))
        records=cursor.fetchall()
        print("Printing the hospital records: ")

 
        for i in records:
            print("Hospital Id: ",i[0])
            print("Hospital Name: ",i[1])
            print("Bed Count: ",i[2])

        close_connection(connection)

    except (Exception, mysql.connector.Error) as error:
            print("Error while getting data", error)

def get_doctor_details(doctor_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = "SELECT * FROM Doctor where Doctor_Id = %s"""
        cursor.execute(select_query, (doctor_id,))
        records = cursor.fetchall()
        print("Printing Doctor records: ")

        for j in records:
            print("Doctor Id:", j[0])
            print("Doctor Name:", j[1])
            print("Hospital Id:", j[2])
            print("Joining Date:", j[3])
            print("Specialty:", j[4])
            print("Salary:", j[5])
            print("Experience:", j[6])

        close_connection(connection)

    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)


print("Question 2: Read given hospital and doctor details \n")
get_hospital_details(4)
print("\n")
print("--------------------------------------------------")

get_doctor_details(107)

    