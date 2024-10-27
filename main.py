import mysql.connector
import random
import re

# Database connection
host = "localhost"
user = "root"
password = "admintomas17"
database = "flight_aware2"

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

## Basic Read Data Queries

    ## Read Plane Table
    def read_data_plane():
        select_query = "SELECT PlaneID, PlaneModel, AirlineCode FROM Plane;"
        cursor.execute(select_query)
        planes = cursor.fetchall()
        print("Plane Data:")
        for plane in planes:
            print(f"Plane ID: {plane[0]} | Plane Model: {plane[1]} | Airline: {plane[2]}")
    
    ## Read Airline Table
    def read_data_airline():
        select_query = "SELECT AirlineName, AirlineCode, Country FROM Airline;"
        cursor.execute(select_query)
        airlines = cursor.fetchall()
        print("Airline Data:")
        for airline in airlines:
            print(f"Airline Name: {airline[0]} | Airline Code: {airline[1]} | Country: {airline[2]}")
    
    ## Read Flight Table
    def read_data_flight():
        select_query = "SELECT AirlineCode, FlightNum, PlaneID, DepartingAirportCode, ArrivingAirportCode, Date, Status FROM Flight;"
        cursor.execute(select_query)
        flights = cursor.fetchall()
        print("Flight Data:")
        for flight in flights:
            print(f"Airline: {flight[0]} | Flight Number: {flight[1]} | Plane ID: {flight[2]} | Departing: {flight[3]} | Arriving: {flight[4]} | Date: {flight[5]} | Status: {flight[6]}")
    #read_data_flight()
    
    ## Read Airport Table
    def read_data_airport():
        select_query = "SELECT AirportName, AirportCode, Location FROM Airport;"
        cursor.execute(select_query)
        airports = cursor.fetchall()
        print("Airport Data:")
        for airport in airports:
            print(f"Aiport Name: {airport[0]} | Airport Code: {airport[1]} | Location: {airport[2]}")

    ## Read Passenger Table
    def read_data_passenger():
        select_query = "SELECT LastName, FirstName, PassportID FROM Passenger;"
        cursor.execute(select_query)
        passengers = cursor.fetchall()
        print("Passenger Data:")
        for passenger in passengers:
            print(f"Name: {passenger[1]} {passenger[0]} | Passport ID: {passenger[2]}")
    
    ## Read Booking Table
    def read_data_booking():
        select_query = "SELECT BookingID, PassengerID, FlightID, SeatNumber, Date FROM Booking;"
        cursor.execute(select_query)
        bookings = cursor.fetchall()
        print("Booking Data:")
        for booking in bookings:
            print(f"Booking Number: {booking[0]} Passenger ID: {booking[1]} | Flight ID: {booking[2]} | Seat Number: {booking[3]} | Date: {booking[4]}")

## Update data

## Insert Data

    ## Functions to help with the insert functions
    def select_airline():

        # Define a dictionary mapping user input to airline names and actions
        airlines = {
            1: "American",
            2: "Delta",
            3: "United",
            4: "Southwest",
            5: "Alaska",
            6: "JetBlue",
            7: "Spirit",
            8: "Frontier",
            9: "Hawaiian",
            10: "Allegiant"
        }

        # Define a function to simulate different behaviors based on the airline selection
        def handle_airline_selection(selection):
            # Define airline codes inside this function and return the selected airline code
            match selection:
                case 1:
                    print("You selected American.")
                    return "AA"
                case 2:
                    print("You selected Delta.")
                    return "DL"
                case 3:
                    print("You selected United.")
                    return "UA"
                case 4:
                    print("You selected Southwest.")
                    return "WN"
                case 5:
                    print("You selected Alaska.")
                    return "AS"
                case 6:
                    print("You selected JetBlue.")
                    return "B6"
                case 7:
                    print("You selected Spirit.")
                    return "NK"
                case 8:
                    print("You selected Frontier.")
                    return "F9"
                case 9:
                    print("You selected Hawaiian.")
                    return "HA"
                case 10:
                    print("You selected Allegiant.")
                    return "G4"
        
        while True:  # Keep prompting the user until they provide valid input
            # Display airline list with corresponding numbers
            print("Please select an airline by entering the corresponding number:")
            for number, airline in airlines.items():
                print(f"{number}. {airline}")
            
            try:
                # Get the user's choice and convert to integer
                choice = int(input("Enter the number of the airline: "))
                
                # Handle the airline selection and return the code if valid
                if choice in airlines:
                    return handle_airline_selection(choice)
                else:
                    print("Invalid selection. Please select a valid number between 1 and 10.")
                    
            except ValueError:
                print("Invalid input. Please enter a valid number between 1 and 10.")
    
    def get_date():
            while True:
                month = input("Enter the month (MM): ").zfill(2)
                if month.isdigit() and 1 <= int(month) <= 12:
                    break
                else:
                    print("Invalid month. Please enter a valid month (01-12).")
            
            while True:
                day = input("Enter the day (DD): ").zfill(2)
                if day.isdigit() and 1 <= int(day) <= 31:
                    break
                else:
                    print("Invalid day. Please enter a valid day (01-31).")
            
            while True:
                year = input("Enter the year (YYYY): ")
                if year.isdigit() and len(year) == 4:
                    break
                else:
                    print("Invalid year. Please enter a valid 4-digit year.")
            
            return f"{year}-{month}-{day}"  # MySQL prefers YYYY-MM-DD format

    ## Insert Passenger Data
    def insert_flight_data():
        # Prompt the user to enter flight data
        airlineCode = select_airline()

        while True:
            flightNumDigits = input("Enter flight number (3 digits: '123'): ").strip()
            if flightNumDigits.isdigit() and len(flightNumDigits) == 3:
                break
            else:
                print("Invalid input. Please enter exactly 3 digits.")
        
        flightNumber = airlineCode + flightNumDigits

        def get_airport_code(location):
            while True:
                airportCode = input(f"Enter {location} airport code (3 letters): ").strip().upper()
                if airportCode.isalpha() and len(airportCode) == 3:
                    return airportCode
                else:
                    print("Invalid input. Please enter exactly 3 letters.")
        
        departingAirportCode = get_airport_code("Departing")
        arrivingAirportCode = get_airport_code("Arriving")
        planeID = f"301 {airlineCode}"
        flightDate = get_date()
        insert_query = """
            INSERT INTO Flight (AirlineCode, FlightNum, PlaneID, DepartingAirportCode, ArrivingAirportCode, Date, Status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        
        # Prepare data to insert
        flight_data = (airlineCode, flightNumber, planeID, departingAirportCode, arrivingAirportCode, flightDate, "On Time")

        # Execute the query
        try:
            cursor.execute(insert_query, flight_data)
            connection.commit()  # Commit transaction
            print("Flight data inserted successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()  # Roll back if any error occurs

    ## Insert Booking Data
    def insert_booking_data():
        passsengerID = input("Enter PassengerID: ")
        flightID = input("Enter FlightID: ")
        seatNum = input("Enter seat number: eg.(32c)")
        date = get_date()
        
        ## Create Query
        insert_query = """
            INSERT INTO Booking (PassengerID, FlightID, SeatNumber, Date)
            VALUES (%s, %s, %s, %s)
        """
        # Prepare data to insert
        booking_data = (passsengerID, flightID, seatNum, date)
        # Execute the query
        try:
            cursor.execute(insert_query, booking_data)
            connection.commit()  # Commit transaction
            print("Booking data inserted successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()  # Roll back if any error occurs
    
    ## Insert Passenger  
    def insert_passenger_data():
        firstName = input("Enter passenger legal first name: ")
        lastName = input("Enter passenger legal last name: ")

        # Validate passportID format: one letter followed by exactly eight digits
        while True:
            passportID = input("Enter passenger's passportID (format: X########): ")
            if re.fullmatch(r"[A-Za-z]\d{8}", passportID):
                break  # Valid passportID format, exit the loop
            else:
                print("Invalid PassportID format. Please enter one letter followed by 8 digits (e.g., A12345678).")

        # Create Query
        insert_query = """
            INSERT INTO Passenger (LastName, FirstName, PassportID)
            VALUES (%s, %s, %s)
        """
        # Prepare data to insert
        passenger_data = (lastName, firstName, passportID)
        
        # Execute the query
        try:
            cursor.execute(insert_query, passenger_data)
            connection.commit()  # Commit transaction
            print("Passenger data inserted successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()  # Roll back if any error occurs

    ## Insert Airport
    def insert_airport_data():
        airport_code = input("Enter the 2-character airport code: ").upper()

        # Validate airport code format: exactly two uppercase characters
        while not re.fullmatch(r"[A-Z]{2}", airport_code):
            print("Invalid Airport Code. Please enter exactly two uppercase letters (e.g., 'NY').")
            airport_code = input("Enter the 2-character airport code: ").upper()

        airport_name = input("Enter the airport name: ")
        location = input("Enter the airport location: ")

        # Create query
        insert_query = """
            INSERT INTO Airport (AirportCode, AirportName, Location)
            VALUES (%s, %s, %s)
        """
        # Prepare data to insert
        airport_data = (airport_code, airport_name, location)

        # Execute the query
        try:
            cursor.execute(insert_query, airport_data)
            connection.commit()  # Commit transaction
            print("Airport data inserted successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()  # Roll back if any error occurs

    ## Insert Plane
    def insert_plane_data():
        # Ask for the AirlineCode and validate it to be exactly two uppercase letters
        while True:
            airline_code = input("Enter the 2-character Airline Code: ").upper()
            if re.fullmatch(r"[A-Z]{2}", airline_code):
                break
            else:
                print("Invalid Airline Code. Please enter exactly two uppercase letters (e.g., 'AA').")
        
        # Ask for the three-digit part of the PlaneID and validate it
        while True:
            plane_number = input("Enter the 3-digit plane number: ")
            if re.fullmatch(r"\d{3}", plane_number):
                break
            else:
                print("Invalid plane number. Please enter exactly three digits (e.g., '123').")
        
        # Construct the PlaneID
        plane_id = f"N{plane_number}{airline_code}"
        
        # Ask for the plane model
        plane_model = input("Enter the plane model: ")

        # Create the query
        insert_query = """
            INSERT INTO Plane (PlaneID, PlaneModel, AirlineCode)
            VALUES (%s, %s, %s)
        """
        # Prepare data to insert
        plane_data = (plane_id, plane_model, airline_code)

        # Execute the query
        try:
            cursor.execute(insert_query, plane_data)
            connection.commit()  # Commit transaction
            print("Plane data inserted successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()  # Roll back if any error occurs


## Delete Data

    ## Delete Flight
    def delete_flight():
        try:
            flightNum = input("Enter Flight Number to delete: ")
            deleteQuery = "DELETE FROM Flight WHERE FlightNum = %s"
            cursor.execute(deleteQuery, (flightNum,))
            connection.commit()
            print("Flight deleted successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()
    
    ## Delete Booking
    def delete_booking():
        try:
            bookingID = input("Enter Booking ID to delete: ")
            deleteQuery = "DELETE FROM Booking WHERE BookingID = %s"
            cursor.execute(deleteQuery, (bookingID,))
            connection.commit()
            print("Booking deleted successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()
    
    ## Delete Passenger
    def delete_passenger():
        try:
            passportID = input("Enter passenger's passport number to delete: ")
            deleteQuery = "DELETE FROM Passenger WHERE PassportID = %s"
            cursor.execute(deleteQuery, (passportID,))
            connection.commit()
            print("Passenger deleted successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()

    ## Delete Airport
    def delete_airport():
        try:
            airportCode = input("Eneter airport's code to delete (ABC): ")
            deleteQuery = "DELETE FROM Airport WHERE AirportCode = %s"
            cursor.execute(deleteQuery, (airportCode,))
            connection.commit()
            print("Airport deleted successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()

    ## Delete Plane
    def delete_plane():
        try:
            planeID = input("Enter Plane ID to delete: ")
            deleteQuery = "DELETE FROM Plane WHERE PlaneID = %s"
            cursor.execute(deleteQuery, (planeID,))
            connection.commit()
            print("Plane deleted successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()

    ## Delete Airline
    def delete_airline():
        try:
            airlineCode = input("Enter Airline Code to delete: (XX) ")
            deleteQuery = "DELETE FROM Airline WHERE AirlineCode = %s"
            cursor.execute(deleteQuery, (airlineCode,))
            connection.commit()
            print("Airline deleted successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()

## Advanced Functions (Deliverable 5)

## Main Program
    def select_table():
        print("\nSelect a table:")
        print("1. Planes")
        print("2. Airlines")
        print("3. Flights")
        print("4. Airports")
        print("5. Passengers")
        print("6. Bookings")
        table_choice = input("Enter your table choice: ")
        
        tables = {
            '1': 'Planes',
            '2': 'Airlines',
            '3': 'Flights',
            '4': 'Airports',
            '5': 'Passengers',
            '6': 'Bookings'
        }
        return tables.get(table_choice, None)

    def main():
        while True:
            print("\nMenu:")
            print("1. Read data")
            print("2. Update data")
            print("3. Insert data")
            print("4. Delete data")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '5':
                print("Exiting...")
                break
            
            table = select_table()
            if not table:
                print("Invalid table choice. Please try again.")
                continue

            if choice == '1':
                print(f"Reading from table {table}")
            elif choice == '2':
                print(f"Updating table {table}")
            elif choice == '3':
                print(f"Inserting into table {table}")
            elif choice == '4':
                print(f"Deleting from table {table}")
            else:
                print("Invalid choice. Please try again.")

## Execute
    main()


except mysql.connector.Error as error:
    print("Error connecting to MySQL:", error)
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
