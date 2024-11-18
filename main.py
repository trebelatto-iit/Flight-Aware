import mysql.connector
import random
import re
import pyfiglet


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
    def read_plane():
        select_query = "SELECT PlaneID, PlaneModel, AirlineCode FROM Plane;"
        cursor.execute(select_query)
        planes = cursor.fetchall()
        print("Plane Data:")
        for plane in planes:
            print(f"Plane ID: {plane[0]} | Plane Model: {plane[1]} | Airline: {plane[2]}")
    
    ## Read Airline Table
    def read_airline():
        select_query = "SELECT AirlineName, AirlineCode, Country FROM Airline;"
        cursor.execute(select_query)
        airlines = cursor.fetchall()
        print("Airline Data:")
        for airline in airlines:
            print(f"Airline Name: {airline[0]} | Airline Code: {airline[1]} | Country: {airline[2]}")
    
    ## Read Flight Table
    def read_flight():
        select_query = "SELECT AirlineCode, FlightNum, PlaneID, DepartingAirportCode, ArrivingAirportCode, Date, Status FROM Flight;"
        cursor.execute(select_query)
        flights = cursor.fetchall()
        print("Flight Data:")
        for flight in flights:
            print(f"Airline: {flight[0]} | Flight Number: {flight[1]} | Plane ID: {flight[2]} | Departing: {flight[3]} | Arriving: {flight[4]} | Date: {flight[5]} | Status: {flight[6]}")
    
    ## Read Airport Table
    def read_airport():
        select_query = "SELECT AirportName, AirportCode, Location FROM Airport;"
        cursor.execute(select_query)
        airports = cursor.fetchall()
        print("Airport Data:")
        for airport in airports:
            print(f"Aiport Name: {airport[0]} | Airport Code: {airport[1]} | Location: {airport[2]}")

    ## Read Passenger Table
    def read_passenger():
        select_query = "SELECT LastName, FirstName, PassportID FROM Passenger;"
        cursor.execute(select_query)
        passengers = cursor.fetchall()
        print("Passenger Data:")
        for passenger in passengers:
            print(f"Name: {passenger[1]} {passenger[0]} | Passport ID: {passenger[2]}")
    
    ## Read Booking Table
    def read_booking():
        select_query = "SELECT BookingID, PassengerID, FlightID, SeatNumber, Date FROM Booking;"
        cursor.execute(select_query)
        bookings = cursor.fetchall()
        print("Booking Data:")
        for booking in bookings:
            print(f"Booking Number: {booking[0]} Passenger ID: {booking[1]} | Flight ID: {booking[2]} | Seat Number: {booking[3]} | Date: {booking[4]}")

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
            print("\nPlease select an airline by entering the corresponding number:")
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
    def insert_flight():
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
        planeNum = random.randint(100, 999)
        planeID = f"N{planeNum}{airlineCode}"
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
    def insert_booking():
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
    def insert_passenger():
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
    def insert_airport():
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
    def insert_plane():
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

    ## Insert Airline
    def insert_airport():
        # Validate airport code format: exactly three uppercase characters
        while True:
            airport_code = input("Enter the 3-character airport code: ").upper()
            if re.fullmatch(r"[A-Z]{3}", airport_code):
                break
            else:
                print("Invalid Airport Code. Please enter exactly three uppercase letters (e.g., 'JFK').")

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
   
    ## Update Booking
    def update_booking():
        # Get the BookingID to identify the record to update
        booking_id = input("Enter BookingID to update: ")

        # Collect new information for the booking
        passenger_id = input("Enter new PassengerID: ")
        flight_id = input("Enter new FlightID: ")
        
        # Validate SeatNumber format, e.g., 32C
        while True:
            seat_num = input("Enter new seat number (e.g., 32C): ").upper()
            if re.fullmatch(r"\d{1,2}[A-Z]", seat_num):
                break
            else:
                print("Invalid seat number format. Please enter a number followed by a letter (e.g., 32C).")

        # Get and validate the date
        date = get_date()  # Assuming get_date() is a function that handles date input validation

        # Create update query
        update_query = """
            UPDATE Booking
            SET PassengerID = %s, FlightID = %s, SeatNumber = %s, Date = %s
            WHERE BookingID = %s
        """
        
        # Prepare data to update
        booking_data = (passenger_id, flight_id, seat_num, date, booking_id)

        # Execute the query
        try:
            cursor.execute(update_query, booking_data)
            connection.commit()  # Commit transaction
            if cursor.rowcount > 0:
                print("Booking data updated successfully.")
            else:
                print("No booking found with the provided BookingID.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()  # Roll back if any error occurs

    ## Update Flight
    def update_flight():
        flight_num = input("Enter Flight Number to update: ")
        # Validate AirlineCode format: exactly two uppercase letters
        while True:
            airline_code = input("Enter new airline code (2 letters): ").upper()
            if re.fullmatch(r"[A-Z]{2}", airline_code):
                break
            else:
                print("Invalid Airline Code. Please enter exactly two uppercase letters (e.g., 'AA').")

        # Validate PlaneID format: "N###XX" where XX matches the airline code
        while True:
            plane_id = input(f"Enter new plane ID (format: N###{airline_code}): ").upper()
            if re.fullmatch(rf"N\d{{3}}{airline_code}", plane_id):
                break
            else:
                print(f"Invalid PlaneID format. Please enter in the format N###{airline_code} (e.g., N123{airline_code}).")

        # Validate DepartingAirportCode format: exactly three uppercase letters
        while True:
            departing = input("Enter new departing airport code (3 letters): ").upper()
            if re.fullmatch(r"[A-Z]{3}", departing):
                break
            else:
                print("Invalid Departing Airport Code. Please enter exactly three uppercase letters (e.g., 'JFK').")

        # Validate ArrivingAirportCode format: exactly three uppercase letters
        while True:
            arriving = input("Enter new arriving airport code (3 letters): ").upper()
            if re.fullmatch(r"[A-Z]{3}", arriving):
                break
            else:
                print("Invalid Arriving Airport Code. Please enter exactly three uppercase letters (e.g., 'LAX').")

        # Get and validate date
        print("Enter new date: ")
        date = get_date()

        # Ensure Status is only text (remove any numeric or special characters for simplicity)
        status = input("Enter new status (letters only): ")
        if not status.isalpha():
            print("Warning: Status should contain only letters. Please enter letters only.")

        # Prepare the update query
        update_query = """
            UPDATE Flight 
            SET AirlineCode = %s, PlaneID = %s, DepartingAirportCode = %s, 
                ArrivingAirportCode = %s, Date = %s, Status = %s 
            WHERE FlightNum = %s;
        """
        # Execute the query
        try:
            cursor.execute(update_query, (airline_code, plane_id, departing, arriving, date, status, flight_num))
            connection.commit()
            print("Data updated successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()  # Roll back if any error occurs

            ## Update data

    ## Update Plane
    def update_plane():
        plane_id = input("Enter Plane ID to update: ")
        # Validate AirlineCode format: must be exactly two uppercase letters
        while True:
            airline = input("Enter new airline associated with the plane (2-letter code): ").upper()
            if re.fullmatch(r"[A-Z]{2}", airline):
                break
            else:
                print("Invalid Airline Code. Please enter exactly two uppercase letters (e.g., 'AA').")

        # Prepare the update query
        update_query = "UPDATE Plane SET AirlineCode = %s WHERE PlaneID = %s"
        
        # Execute the query
        try:
            cursor.execute(update_query, (airline, plane_id))
            connection.commit()
            print("Data updated successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()  # Roll back if any error occurs

    ## Update Airline
    def update_airport():
        # Validate airport code format: exactly three uppercase letters
        while True:
            airport_code = input("Enter the 3-character airport code to update: ").upper()
            if re.fullmatch(r"[A-Z]{3}", airport_code):
                break
            else:
                print("Invalid Airport Code. Please enter exactly three uppercase letters (e.g., 'JFK').")

        # Collect new information for the airport
        airport_name = input("Enter the new airport name: ")
        location = input("Enter the new airport location: ")

        # Create update query
        update_query = """
            UPDATE Airport
            SET AirportName = %s, Location = %s
            WHERE AirportCode = %s
        """
        # Prepare data to update
        airport_data = (airport_name, location, airport_code)

        # Execute the query
        try:
            cursor.execute(update_query, airport_data)
            connection.commit()  # Commit transaction
            if cursor.rowcount > 0:
                print("Airport data updated successfully.")
            else:
                print("No airport found with the provided AirportCode.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()  # Roll back if any error occurs

    ## Update Passenger
    def update_passenger():
        # Validate PassportID format: one letter followed by exactly eight digits
        while True:
            passport_id = input("Enter the passenger's PassportID to update (format: X########): ")
            if re.fullmatch(r"[A-Za-z]\d{8}", passport_id):
                break
            else:
                print("Invalid PassportID format. Please enter one letter followed by 8 digits (e.g., A12345678).")

        # Collect new information for the passenger
        first_name = input("Enter new legal first name: ")
        last_name = input("Enter new legal last name: ")

        # Create update query
        update_query = """
            UPDATE Passenger
            SET FirstName = %s, LastName = %s
            WHERE PassportID = %s
        """
        # Prepare data to update
        passenger_data = (first_name, last_name, passport_id)

        # Execute the query
        try:
            cursor.execute(update_query, passenger_data)
            connection.commit()  # Commit transaction
            if cursor.rowcount > 0:
                print("Passenger data updated successfully.")
            else:
                print("No passenger found with the provided PassportID.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()  # Roll back if any error occurs

## Delete Data

    ## Delete Flight
    def delete_flight():
        try:
            flight_num = input("Enter Flight Number to delete: ")
            delete_query = "DELETE FROM Flight WHERE FlightNum = %s"
            
            cursor.execute(delete_query, (flight_num,))
            connection.commit()
            
            if cursor.rowcount > 0:
                print("Flight deleted successfully.")
            else:
                print("No flight found with the provided Flight Number.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()

    ## Delete Booking
    def delete_booking():
        try:
            booking_id = input("Enter Booking ID to delete: ")
            delete_query = "DELETE FROM Booking WHERE BookingID = %s"
            
            cursor.execute(delete_query, (booking_id,))
            connection.commit()
            
            if cursor.rowcount > 0:
                print("Booking deleted successfully.")
            else:
                print("No booking found with the provided Booking ID.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()

    ## Delete Passenger
    def delete_passenger():
        try:
            passport_id = input("Enter passenger's passport number to delete: ")
            delete_query = "DELETE FROM Passenger WHERE PassportID = %s"
            
            cursor.execute(delete_query, (passport_id,))
            connection.commit()
            
            if cursor.rowcount > 0:
                print("Passenger deleted successfully.")
            else:
                print("No passenger found with the provided Passport ID.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()

    ## Delete Airport
    def delete_airport():
        try:
            airport_code = input("Enter airport's code to delete (ABC): ")
            delete_query = "DELETE FROM Airport WHERE AirportCode = %s"
            
            cursor.execute(delete_query, (airport_code,))
            connection.commit()
            
            if cursor.rowcount > 0:
                print("Airport deleted successfully.")
            else:
                print("No airport found with the provided Airport Code.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()

    ## Delete Plane
    def delete_plane():
        try:
            plane_id = input("Enter Plane ID to delete: ")
            delete_query = "DELETE FROM Plane WHERE PlaneID = %s"
            
            cursor.execute(delete_query, (plane_id,))
            connection.commit()
            
            if cursor.rowcount > 0:
                print("Plane deleted successfully.")
            else:
                print("No plane found with the provided Plane ID.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()

    ## Delete Airline
    def delete_airline():
        try:
            airline_code = input("Enter Airline Code to delete (XX): ")
            delete_query = "DELETE FROM Airline WHERE AirlineCode = %s"
            
            cursor.execute(delete_query, (airline_code,))
            connection.commit()
            
            if cursor.rowcount > 0:
                print("Airline deleted successfully.")
            else:
                print("No airline found with the provided Airline Code.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()


    ## Advanced Functions (Deliverable 5)
    def get_top_5_busiest_airports():
            # SQL query to get the top 5 busiest airports
            query = """
            SELECT 
                a.AirportCode,
                a.AirportName,
                COUNT(f.FlightID) AS TotalFlights
            FROM 
                airport a
            JOIN 
                flight f ON a.AirportCode = f.DepartingAirportCode OR a.AirportCode = f.ArrivingAirportCode
            GROUP BY 
                a.AirportCode, a.AirportName
            ORDER BY 
                TotalFlights DESC
            LIMIT 5;
            """

            # Execute the query
            cursor.execute(query)

            # Fetch and return the results
            results = cursor.fetchall()
            for row in results:
                print(f"Airport Code: {row[0]}, Airport Name: {row[1]}, Total Flights: {row[2]}")

    def get_top_10_frequent_fliers():
        # SQL query to get the top 10 frequent fliers
        query = """
        SELECT 
            p.PassengerID,
            p.FirstName,
            p.LastName,
            COUNT(b.BookingID) AS TotalBookings
        FROM 
            passenger p
        JOIN 
            booking b ON p.PassengerID = b.PassengerID
        GROUP BY 
            p.PassengerID, p.FirstName, p.LastName
        ORDER BY 
            TotalBookings DESC
        LIMIT 10;
        """

        # Execute the query using the global cursor
        cursor.execute(query)

        # Fetch the results
        results = cursor.fetchall()

        # Print the results
        for row in results:
            print(f"Passenger ID: {row[0]}, Name: {row[1]} {row[2]}, Total Bookings: {row[3]}")
    
    def get_flight_history_for_passenger():
        # Prompt the user for a passenger ID
        passenger_id = input("Enter Passenger ID: ")

        # Check if the ID is valid (exists in the database)
        validation_query = "SELECT COUNT(*) FROM passenger WHERE PassengerID = %s"
        cursor.execute(validation_query, (passenger_id,))
        result = cursor.fetchone()

        if result[0] == 0:
            print("Invalid Passenger ID. Please try again.")
            return

        # SQL query to get the flight history for the valid passenger
        query = """
        SELECT 
            b.BookingID,
            f.FlightNum,
            f.Date,
            f.DepartingAirportCode,
            f.ArrivingAirportCode,
            f.Status,
            p.FirstName,
            p.LastName
        FROM 
            booking b
        JOIN 
            flight f ON b.FlightID = f.FlightID
        JOIN 
            passenger p ON b.PassengerID = p.PassengerID
        WHERE 
            p.PassengerID = %s
        ORDER BY 
            f.Date;
        """

        # Execute the query for the valid passenger ID
        cursor.execute(query, (passenger_id,))

        # Fetch the results
        results = cursor.fetchall()

        # Print the results
        if results:
            print(f"\nFlight history for Passenger ID {passenger_id}:")
            for row in results:
                print(f"Booking ID: {row[0]}, Flight Number: {row[1]}, Date: {row[2]}, "
                    f"From: {row[3]}, To: {row[4]}, Status: {row[5]}, "
                    f"Passenger Name: {row[6]} {row[7]}")
        else:
            print(f"No flight history found for Passenger ID {passenger_id}.")

    # OLAP
    def get_cumulative_total_flights_for_airline():
        # Prompt the user for an airline code
        airline_code = input("Enter Airline Code: ")

        # SQL query to find the cumulative total flights up to each date for an airline
        query = """
        SELECT 
            f.Date,
            COUNT(f.FlightID) AS DailyFlights,
            SUM(COUNT(f.FlightID)) OVER (ORDER BY f.Date) AS CumulativeFlights
        FROM 
            flight f
        WHERE 
            f.AirlineCode = %s
        GROUP BY 
            f.Date
        ORDER BY 
            f.Date;
        """

        # Execute the query using the global cursor
        cursor.execute(query, (airline_code,))

        # Fetch the results
        results = cursor.fetchall()

        # Print the results
        if results:
            print(f"\nCumulative total flights for Airline Code '{airline_code}':")
            for row in results:
                print(f"Date: {row[0]}, Daily Flights: {row[1]}, Cumulative Flights: {row[2]}")
        else:
            print(f"No flight data found for Airline Code '{airline_code}'.")

    def get_moving_average_of_flights_for_airport():
        # Prompt the user for the airport code
        airport_code = input("Enter Airport Code: ")

        # SQL query to calculate the 7-day moving average of flights for the specified airport
        query = """
        SELECT 
            f.DepartingAirportCode,
            f.Date,
            COUNT(f.FlightID) AS DailyFlights,
            AVG(COUNT(f.FlightID)) OVER (
                PARTITION BY f.DepartingAirportCode 
                ORDER BY f.Date 
                ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
            ) AS MovingAvgFlights
        FROM 
            flight f
        WHERE 
            f.DepartingAirportCode = %s
        GROUP BY 
            f.DepartingAirportCode, f.Date
        ORDER BY 
            f.Date;
        """

        # Execute the query using the global cursor
        cursor.execute(query, (airport_code,))

        # Fetch the results
        results = cursor.fetchall()

        # Print the results
        if results:
            print(f"\n7-day moving average of flights for Airport '{airport_code}':")
            for row in results:
                print(f"Date: {row[1]}, Daily Flights: {row[2]}, 7-Day Moving Avg Flights: {row[3]:.2f}")
        else:
            print(f"No flight data available for Airport '{airport_code}'.")

    # Advanced Aggregate Functions
    def get_average_passengers_per_flight_per_day():
        # SQL query to find the average number of passengers per flight per day
        query = """
        SELECT 
            f.Date,
            AVG(subquery.PassengerCount) AS AvgPassengersPerFlight
        FROM 
            flight f
        JOIN (
            SELECT 
                b.FlightID,
                COUNT(b.PassengerID) AS PassengerCount
            FROM 
                booking b
            GROUP BY 
                b.FlightID
        ) subquery ON f.FlightID = subquery.FlightID
        GROUP BY 
            f.Date
        ORDER BY 
            f.Date;
        """

        # Execute the query using the global cursor
        cursor.execute(query)

        # Fetch the results
        results = cursor.fetchall()

        # Print the results
        if results:
            print("\nAverage number of passengers per flight per day:")
            for row in results:
                print(f"Date: {row[0]}, Average Passengers: {row[1]:.2f}")
        else:
            print("No data available for average passengers per flight per day.")

    # Complex Joins and Nested Queries
    def get_flights_with_highest_passenger_count():
        # SQL query to find flights with the highest number of passengers booked
        query = """
        SELECT 
            f.FlightNum,
            f.Date,
            f.DepartingAirportCode,
            f.ArrivingAirportCode,
            booking_count.TotalPassengers
        FROM 
            flight f
        JOIN (
            SELECT 
                b.FlightID,
                COUNT(b.PassengerID) AS TotalPassengers
            FROM 
                booking b
            GROUP BY 
                b.FlightID
        ) booking_count ON f.FlightID = booking_count.FlightID
        ORDER BY 
            booking_count.TotalPassengers DESC
        LIMIT 5;
        """

        # Execute the query using the global cursor
        cursor.execute(query)

        # Fetch the results
        results = cursor.fetchall()

        # Print the results
        if results:
            print("\nFlights with the highest number of passengers booked:")
            for row in results:
                print(f"Flight Number: {row[0]}, Date: {row[1]}, From: {row[2]}, To: {row[3]}, "
                    f"Total Passengers: {row[4]}")
        else:
            print("No data available for flights with passenger counts.")

    # sorted flight info
    def get_flight_information_sorted():
        # Prompt the user to filter by specific criteria
        print("Enter filter criteria (leave blank if not applicable):")
        airport_code = input("Filter by Departing Airport Code: ")
        airline_code = input("Filter by Airline Code: ")
        date = input("Filter by Date (YYYY-MM-DD, or leave blank): ")

        # Prompt the user to select a sorting option
        print("\nChoose a field to sort by:")
        print("1. Airport")
        print("2. Airline")
        print("3. Flight Number")
        print("4. Date")
        
        # Map user input to SQL column names
        sort_options = {
            '1': 'DepartingAirportCode',
            '2': 'AirlineCode',
            '3': 'FlightNum',
            '4': 'Date'
        }

        # Get the user's choice for sorting
        choice = input("Enter the number corresponding to your choice: ")

        # Validate the user's choice
        if choice not in sort_options:
            print("Invalid choice. Please select a valid option.")
            return

        # Store the selected sorting column
        sort_column = sort_options[choice]

        # Base query
        query = """
        SELECT 
            f.FlightNum,
            f.Date,
            f.DepartingAirportCode,
            f.ArrivingAirportCode,
            f.AirlineCode,
            f.Status
        FROM 
            flight f
        WHERE 
            (%s IS NULL OR f.DepartingAirportCode = %s)
            AND (%s IS NULL OR f.AirlineCode = %s)
            AND (%s IS NULL OR f.Date = %s)
        ORDER BY 
            {sort_column};
        """.format(sort_column=sort_column)

        # Execute the query using the global cursor
        cursor.execute(query, (airport_code or None, airport_code or None, 
                            airline_code or None, airline_code or None, 
                            date or None, date or None))

        # Fetch the results
        results = cursor.fetchall()

        # Print the results
        if results:
            print(f"\nFlight information filtered and sorted by {sort_column}:")
            for row in results:
                print(f"Flight Number: {row[0]}, Date: {row[1]}, Departing Airport: {row[2]}, "
                    f"Arriving Airport: {row[3]}, Airline: {row[4]}, Status: {row[5]}")
        else:
            print("No flight data available for the given filters.")

    def get_bookings_by_passenger():
        """
        Prompt the user for a PassengerID and display their bookings.
        Assumes a global database connection.
        """
        try:
            # Prompt the user for PassengerID
            passenger_id = int(input("Enter PassengerID: "))
            
            
            # Query to fetch bookings for the given PassengerID
            query = """
            SELECT 
                booking.BookingID, 
                booking.FlightID, 
                booking.SeatNumber, 
                booking.Date,
                flight.AirlineCode,
                flight.FlightNum,
                flight.DepartingAirportCode,
                flight.ArrivingAirportCode,
                flight.Status
            FROM booking
            JOIN flight ON booking.FlightID = flight.FlightID
            WHERE booking.PassengerID = %s
            """
            
            # Execute the query
            cursor.execute(query, (passenger_id,))
            results = cursor.fetchall()
            
            # Check if any bookings exist
            if not results:
                print(f"No bookings found for PassengerID {passenger_id}.")
                return
            
            # Display the bookings
            print(f"Bookings for PassengerID {passenger_id}:")
            for booking in results:
                print(f"""
                Booking ID: {booking['BookingID']}
                Flight ID: {booking['FlightID']}
                Airline: {booking['AirlineCode']}
                Flight Number: {booking['FlightNum']}
                Departing: {booking['DepartingAirportCode']}
                Arriving: {booking['ArrivingAirportCode']}
                Date: {booking['Date']}
                Seat: {booking['SeatNumber']}
                Status: {booking['Status']}
                """)
        
        except ValueError:
            print("Invalid PassengerID. Please enter a numeric value.")
        except Exception as err:
            print(f"Error: {err}")

    def passengers_with_all_flight_bookings_for_airport():
        """
        Prompt the user for an airport code, validate it, and find passengers who have 
        bookings for all flights departing from that airport.

        Args:
            connection: A MySQL database connection object.

        Returns:
            None: Prints the PassengerIDs and relevant details if found.
        """
        try:
            # Prompt the user for the airport code
            airport_code = input("Enter the departing airport code: ").upper()

            # Validate the airport code
            validation_query = "SELECT AirportCode FROM airport WHERE AirportCode = %s"
            cursor.execute(validation_query, (airport_code,))
            valid_airport = cursor.fetchone()

            if not valid_airport:
                print(f"Invalid airport code: {airport_code}. Please enter a valid code.")
                return

            # Main query to find passengers with bookings for all flights departing from the given airport
            query = """
            SELECT PassengerID
            FROM booking
            WHERE FlightID IN (
                SELECT FlightID 
                FROM flight 
                WHERE DepartingAirportCode = %s
            )
            GROUP BY PassengerID
            HAVING COUNT(DISTINCT FlightID) = (
                SELECT COUNT(DISTINCT FlightID) 
                FROM flight 
                WHERE DepartingAirportCode = %s
            );
            """

            # Execute the main query
            cursor.execute(query, (airport_code, airport_code))
            results = cursor.fetchall()

            # Check if any passengers match the criteria
            if not results:
                print(f"No passengers have bookings for all flights departing from {airport_code}.")
            else:
                print(f"Passengers with bookings for all flights departing from {airport_code}:")
                for row in results:
                    print(f"PassengerID: {row['PassengerID']}")

        except Exception as e:
            print(f"An error occurred: {e}")
   
   ## Set Operation and Aggregate function
    def get_departure_counts_ranked():
        """
        Retrieves and ranks airports by their number of departures.
        """
        try:
            # SQL query using WITH clause to calculate departure counts and rank them
            query = """
            WITH DepartureCounts AS (
                SELECT DepartingAirportCode, COUNT(*) AS DepartureCount
                FROM flight
                GROUP BY DepartingAirportCode
            )
            SELECT DepartingAirportCode, DepartureCount
            FROM DepartureCounts
            ORDER BY DepartureCount DESC;
            """
            
            # Execute the query using the global cursor
            cursor.execute(query)

            # Fetch the results
            results = cursor.fetchall()

            # Print the results
            if results:
                print("\nAirports ranked by number of departures:")
                for row in results:
                    print(f"Airport Code: {row[0]}, Departure Count: {row[1]}")
            else:
                print("No data available for airport departure counts.")
        except Exception as e:
            print(f"An error occurred while retrieving departure counts: {e}")

## Main Program

    def main():
        figlet = pyfiglet.Figlet(font='doom')
        logo = figlet.renderText('FlightAware')
        while True:
            print(logo)
            print("Welcome to Flight Aware!")
            print("\nSelect a Table to start:")
            print("1. Passenger")
            print("2. Airport")
            print("3. Plane")
            print("4. Flight")
            print("5. Booking")
            print("6. Other")
            print("7. Exit")
            table_choice = input("Enter your choice: ")

            if table_choice == '7':
                print(figlet.renderText('THANK YOU!'))
                print("Exiting program.")
                break

            # Map the user choice to table operations
            if table_choice == '1':
                table_name = "Passenger"
                def read():
                    read_passenger()
                def insert():
                    insert_passenger()
                def update():
                    update_passenger()
                def delete():
                    delete_passenger()

            elif table_choice == '2':
                table_name = "Airport"
                def read():
                    read_airport()
                def insert():
                    insert_airport()
                def update():
                    update_airport()
                def delete():
                    delete_airport()

            elif table_choice == '3':
                table_name = "Plane"
                def read():
                    read_plane()
                def insert():
                    insert_plane()
                def update():
                    update_plane()
                def delete():
                    delete_plane()

            elif table_choice == '4':
                table_name = "Flight"
                def read():
                    read_flight()
                def insert():
                    insert_flight()
                def update():
                    update_flight()
                def delete():
                    delete_flight()

            elif table_choice == '5':
                table_name = "Booking"
                def read():
                    read_booking()
                def insert():
                    insert_booking()
                def update():
                    update_booking()
                def delete():
                    delete_booking()

            elif table_choice == '6':
                while True:
                    print("\nOther Operations:")
                    print("1. Get cumulative total flights for an airline")
                    print("2. Get average number of passengers per flight per day")
                    print("3. Get flights with the highest number of passengers booked")
                    print("4. Calculate 7-day moving average of flights for an airport")
                    print("5. Get flight information sorted by user choice")
                    print("6. Get top 5 busiest airports")
                    print("7. Get top 10 frequent fliers")
                    print("8. Get flight history for a passenger")
                    print("9. Get ranked departure counts per airport")
                    print("10. Back to main menu")
                    
                    other_choice = input("Enter your choice: ")

                    if other_choice == '1':
                        get_cumulative_total_flights_for_airline()
                    elif other_choice == '2':
                        get_average_passengers_per_flight_per_day()
                    elif other_choice == '3':
                        get_flights_with_highest_passenger_count()
                    elif other_choice == '4':
                        get_moving_average_of_flights_for_airport()
                    elif other_choice == '5':
                        get_flight_information_sorted()
                    elif other_choice == '6':
                        get_top_5_busiest_airports()
                    elif other_choice == '7':
                        get_top_10_frequent_fliers()
                    elif other_choice == '8':
                        get_flight_history_for_passenger()
                    elif other_choice == '9':
                        get_departure_counts_ranked()
                    elif other_choice == '10':
                        break
                    else:
                        print("Invalid choice. Please select a valid option.")
                continue  
            while True:
                print(f"\n{table_name} Table Operations:")
                print("1. Read data")
                print("2. Insert data")
                print("3. Update data")
                print("4. Delete data")
                print("5. Back to main menu")
                action_choice = input("Enter your choice: ")

                if action_choice == '1':
                    print("Reading data from", table_name)
                    read()
                elif action_choice == '2':
                    insert()
                elif action_choice == '3':
                    update()
                elif action_choice == '4':
                    print("Deleting data from", table_name)
                    delete()
                elif action_choice == '5':
                    break
                else:
                    print("Invalid choice. Please select a valid option.")


    ## Execute Main Application
    main()

except mysql.connector.Error as error:
    print("Error connecting to MySQL:", error)
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
