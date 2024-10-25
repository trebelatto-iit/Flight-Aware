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
    
    #read_data_plane()

    ## read airline table
    def read_data_airline():
        select_query = "SELECT AirlineName, AirlineCode, Country FROM Airline;"
        cursor.execute(select_query)
        airlines = cursor.fetchall()
        print("Airline Data:")
        for airline in airlines:
            print(f"Airline Name: {airline[0]} | Airline Code: {airline[1]} | Country: {airline[2]}")
    #read_data_airline()

    ## read flight table
    def read_data_flight():
        select_query = "SELECT FlightNum, AirlineID, PlaneID, DepartingAirportCode, ArrivingAirportCode, Date, Status FROM Flight;"
        cursor.execute(select_query)
        flights = cursor.fetchall()
        print("Flight Data:")
        for flight in flights:
            print(f"Flight Number: {flight[0]} | Airline ID: {flight[1]} | Plane ID: {flight[2]} | Departing: {flight[3]} | Arriving: {flight[4]} | Date: {flight[5]} | Status: {flight[6]}")
    #read_data_flight()

    ## read airport table
    def read_data_airport():
        select_query = "SELECT AirportName, AirportCode, Location FROM Airport;"
        cursor.execute(select_query)
        airports = cursor.fetchall()
        print("Airport Data:")
        for airport in airports:
            print(f"Aiport Name: {airport[0]} | Airport Code: {airport[1]} | Location: {airport[2]}")
    #read_data_airport()

    ## read passenger table
    def read_data_passenger():
        select_query = "SELECT LastName, FirstName, PassportID FROM Passenger;"
        cursor.execute(select_query)
        passengers = cursor.fetchall()
        print("Passenger Data:")
        for passenger in passengers:
            print(f"Name: {passenger[1]} {passenger[0]} | Passport ID: {passenger[2]}")
    #read_data_passenger()

    ## read booking table
    def read_data_booking():
        select_query = "SELECT PassengerID, FlightID, SeatNumber, Date FROM Booking;"
        cursor.execute(select_query)
        bookings = cursor.fetchall()
        print("Booking Data:")
        for booking in bookings:
            print(f"Passenger ID: {booking[0]} | Flight ID: {booking[1]} | Seat Number {booking[2]} | Date: {booking[3]}")
    #read_data_booking()

## more advanced read queries

## update data

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

    def insert_flight_data():
        airlineCode = select_airline()  # Get the airline code

        # Loop until valid input (3 digits) is entered
        while True:
            flightNumDigits = input("Enter flight number (3 digits: '123'): ")
            # Check if the input is exactly 3 digits
            if flightNumDigits.isdigit() and len(flightNumDigits) == 3:
                break  # Exit loop if the input is valid
            else:
                print("Invalid input. Please enter exactly 3 digits.")
        
        flightNumber = airlineCode + flightNumDigits  # Combine airline code and flight number
        def get_airport_code(location):
            # Loop until valid input (3 letters) is entered
            while True:
                airportCode = input("Enter " + location + " airport code (3 letters): ").upper()  # Convert input to uppercase
                # Check if the input is exactly 3 letters
                if airportCode.isalpha() and len(airportCode) == 3:
                    return airportCode  # Return the valid airport code
                else:
                    print("Invalid input. Please enter exactly 3 letters.")
        departingAirportCode = get_airport_code("Departing")
        arrivingAirportCode = get_airport_code("Arriving")
        def get_date():
            # Loop to get valid month
            while True:
                month = input("Enter the month (MM): ").zfill(2)  # Ensure 2 digits by zero-padding
                # Check if input is a digit and between 1 and 12
                if month.isdigit() and 1 <= int(month) <= 12:
                    break
                else:
                    print("Invalid month. Please enter a valid month (01-12).")

            # Loop to get valid day
            while True:
                day = input("Enter the day (DD): ").zfill(2)  # Ensure 2 digits by zero-padding
                # Check if input is a digit and between 1 and 31
                if day.isdigit() and 1 <= int(day) <= 31:
                    break
                else:
                    print("Invalid day. Please enter a valid day (01-31).")
            
            # Loop to get valid year
            while True:
                year = input("Enter the year (YYYY): ")
                # Check if input is a 4-digit year
                if year.isdigit() and len(year) == 4:
                    break
                else:
                    print("Invalid year. Please enter a valid 4-digit year.")
            
            # Combine month, day, and year into MM/DD/YYYY format
            date = f"{month}/{day}/{year}"
            
            return date

        # Example usage
        formattedDate = get_date()
        print(f"Flight Number: {flightNumber} | Departing Airport: {departingAirportCode} | Arriving Airport: {arrivingAirportCode} | Date: {formattedDate}")
        
    insert_flight_data()






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
## Execute


except mysql.connector.Error as error:
    print("Error connecting to MySQL:", error)
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()




