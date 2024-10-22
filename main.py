import mysql.connector
import pyfiglet

# Database connection
host = "localhost"
user = "root"
password = "admintomas17"
database = "flight_aware"

try:
    # Connect to mysql
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connected successfully")

    cursor = connection.cursor()

    # read data queries

    ## read plane table
    def read_data_plane():
        select_query = "SELECT PlaneID, PlaneModel, Airline FROM Plane;"
        cursor.execute(select_query)
        planes = cursor.fetchall()
        print("Plane Data:")
        for plane in planes:
            print(f"PlaneID: {plane[0]} | PlaneModel: {plane[1]} | Airline: {plane[2]}")

    ## read airline table
    def read_data_airline():
        select_query = ""
        cursor.execute(select_query)

    ## read flight table
    def read_data_flight():
        select_query = ""
        cursor.execute(select_query)

    ## read airport table
    def read_data_airport():
        select_query = ""
        cursor.execute(select_query)






except mysql.connector.Error as error:
    print("Error connecting to MySQL:", error)
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()

