import mysql.connector
import pyfiglet

# Database connection
host = "localhost"
user = "root"
password = ""
database = ""

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

