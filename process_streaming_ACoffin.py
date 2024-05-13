"""
Custom Python Script created to demonstrate loading an SQLite database using MTA Data.
Created by: Alexandra Coffin
Northwest Missouri State University
----

MTA Data is readily available from New York State from their Portal. 
In this instance the CSV file has been modified to split data and time.
Additionally, time was converted to military time for the sake of loading into the database.

See README for details on original Dataset and notes on modifications.
NYC MTA Data for Subways: https://data.ny.gov/Transportation/MTA-Subway-Hourly-Ridership-Beginning-February-202/wujg-7c2s/about_data
---
To learn about logging and automating terminal readouts as text files reference the following: https://realpython.com/python-logging/
---

Streaming process: use port 9999

Create a fake stream of data using modified sample of original MTA Data, MTAHourlyData50R.csv.
Revers the order of the rows to read the data from OLDEST first.

Important!

This process will stream forever, or until the end of the rile is read.
Use Ctrl-C to Stop.

"""


# Import from Python Standard Library:
import csv
import socket
import time
import logging


# Set up basic configuration for logging, including creating an output file.
# Using both the filemode='w' and filename allows us to write terminal information directly as a text file. 
logging.basicConfig(
   #filename="out9.txt", filemode= 'w', level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
   filename="out9.txt", filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s'
)

# Declare program constants: Host, Port, Address_tuple and input_file
HOST = "localhost"
PORT = 9999
ADDRESS_TUPLE = (HOST, PORT)
INPUT_FILE_NAME = "MTAHourlyData50R.csv"
OUTPUT_FILE_NAME = "out9.txt"

# Defining Program functions: 
def prepare_message_from_row(row):
    """Prepare a binary message from a given row."""
    transit_date, transit_time, transit_mode, station_complex_id, station_complex, borough, payment_method, fare_class_category, ridership, transfers, latitude, longitude, Georeference = row
    fstring_message = f"{transit_date}, {transit_time}, {transit_mode}, {station_complex_id}, {station_complex}, {borough}, {payment_method}, {fare_class_category}, {ridership}, {transfers}, {latitude}, {longitude}, {Georeference}"

    # Encoding the f-strig to create binary message to stream
    MESSAGE = fstring_message.encode()
    logging.debug(f"Prepared Message: {fstring_message}")
    return MESSAGE

# Reading file object (r = read)
# Stream Created Data
def stream_row(input_file_name, output_file_name, address_tuple):
    logging.info(f"Starting to stream data from {input_file_name} to {address_tuple} and generate {output_file_name}.")
    try:
        #with open(input_file_name, "r") as input_file:
        with open(input_file_name, "r") as input_file:
            logging.info(f"Opened for reading: {input_file}.")
            reader = csv.reader(input_file, delimiter=",")
            # Skips the Header
            header = next(reader)
            logging.info(f"Skipped Header Row: {header}")
            
            with  open(output_file_name, "w") as output_file:
                logging.info(f"Write's output to {output_file_name}")
                writer = csv.writer(output_file, delimiter=",")
                writer.writerow(["transit_date", "transit_time", "transit_mode", "station_complex_id", "station_complex", "borough", "payment_method", "fare_class_category", "ridership", "transfers", "latitude", "longitude", "Georeference"])
                for row in reader:
                    transit_date, transit_time, transit_mode, station_complex_id, station_complex, borough, payment_method, fare_class_category, ridership, transfers, latitude, longitude, Georeference = row
                    writer.writerow([transit_date, transit_time, transit_mode, station_complex_id, station_complex, borough, payment_method, fare_class_category, ridership, transfers, latitude, longitude, Georeference])
                                
            # Configuring socket types, set address family to IPV4
            # Set socket type to UDP for datagram and rappid exicution.
            ADDRESS_FAMILY = socket.AF_INET
            SOCKET_TYPE = socket.SOCK_DGRAM
            
            # Call the socket constructor, socket.socket()
            # Use constructor to make new socket object.
            # New Varriable Assigned to socket object = "sock_object".
            sock_object = socket.socket(ADDRESS_FAMILY, SOCKET_TYPE)

            for row in reader:
                MESSAGE = prepare_message_from_row(row)
                sock_object.sendto(MESSAGE, ADDRESS_TUPLE)
                output_file.write(','.join(row) + '\n')
                output_file.flush()
                time.sleep(3) # Wait 3 seconds between messages.
                # Updating logging info:
                logging.info(f"Sent: {','.join(row)}. Hit CTRL-C to Stop.")
    except FileNotFoundError:
        logging.error(f"File {input_file} not found.")
    except Exception as e:
        logging.error(f" An error occured: {e}")
    finally:
        if 'sock_object' in locals:
            sock_object.close()
if __name__ == "__main__":
    try:
        logging.info("=======================================================")
        logging.info("Starting fake streaming process.")
        stream_row(INPUT_FILE_NAME, OUTPUT_FILE_NAME, ADDRESS_TUPLE)
        logging.info("Streaming Complete!")
        logging.info("=======================================================")
    except Exception as e:
        logging.error(f"An error occured: {e}")
