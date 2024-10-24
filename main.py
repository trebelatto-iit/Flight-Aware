import mysql.connector

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

## basic read data queries

    ## read plane table
    def read_data_plane():
        select_query = "SELECT PlaneID, PlaneModel, Airline FROM Plane;"
        cursor.execute(select_query)
        planes = cursor.fetchall()
        print("Plane Data:")
        for plane in planes:
            print(f"Plane ID: {plane[0]} | Plane Model: {plane[1]} | Airline: {plane[2]}")

    ## read airline table
    def read_data_airline():
        select_query = "SELECT AirlineName, AirlineCode, Country FROM Airline;"
        cursor.execute(select_query)
        airlines = cursor.fetchall()
        print("Airline Data:")
        for airline in airlines:
            print(f"Airline Name: {airline[0]} | Airline Code: {airline[1]} | Country: {airline[2]}")

    ## read flight table
    def read_data_flight():
        select_query = "SELECT FlightNum, AirlineID, PlaneID, DepartingAirportCode, ArrivingAirportCode, Date, Status FROM Flight;"
        cursor.execute(select_query)
        flights = cursor.fetchall()
        print("Flight Data:")
        for flight in flights:
            print(f"Flight Number: {flight[1]} | Airline ID: {flight[0]} | Plane ID: {flight[2]} | Departing: {flight[3]} | Arriving: {flight[4]} | Date: {flight[5]} | Status: {flight[6]}")

    ## read airport table
    def read_data_airport():
        select_query = ""
        cursor.execute(select_query)
        airports = cursor.fetchall()
        print("Airport Data:")
        for airport in airports:
            print(f"Aiport Name: {airport[0]} | Airport Code: {airport[1]} | Location: {airport[2]}")


    ## read passenger table
    def read_data_passenger():
        select_query = ""
        cursor.execute(select_query)
        passengers = cursor.fetchall()
        print("Passenger Data:")
        for passenger in passengers:
            print(f"First Name: {passenger[1]} | Last Name: {passenger[0]} | Passport ID: {passenger[2]}")

    ## read booking table
    def read_data_booking():
        select_query = ""
        cursor.execute(select_query)
        bookings = cursor.fetchall()
        print("Booking Data:")
        for booking in bookings:
            print(f"Passenger ID: {booking[0]} | Flight ID: {booking[1]} | Seat Number {booking[2]} | Date: {booking[3]}")

## more advanced read queries

## update data 

## delete data

## advanced functions

## Main Program

    def main():
            while True:
                print("\nMenu:")
                print("1. read data")
                print("2. update data")
                print("3. insert data")
                print("4. delete data")
                print("5. basic functions")
                print("6. advanced functions")
                print("7. exit")
                choice = input("Enter your choice: \n")

                ## determine what to do with given choice using above functions
           
    read_data_airport()

except mysql.connector.Error as error:
    print("Error connecting to MySQL:", error)
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()

## Execute



