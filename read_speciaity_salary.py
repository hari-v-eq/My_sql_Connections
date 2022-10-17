#Exercise 3: Get the list Of doctors as per the given specialty and salary


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


def get_specialist_doctors_list(speciality, salary):
    try:
        connection=get_connection()
        cursor=connection.cursor()
        select_query="SELECT * FROM Doctor WHERE Speciality = %s and Salary>=%s"
        cursor.execute(select_query,(speciality, salary))
        records=cursor.fetchall()

        print("Printing doctors whose specialty is", speciality, "and salary greater than", salary, "\n")

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

print(" Exercise 3: Get the list Of doctors as per the given specialty and salary: ")
print("-------------------------------------------------------------------------------")
get_specialist_doctors_list("Radiologist",20000)



