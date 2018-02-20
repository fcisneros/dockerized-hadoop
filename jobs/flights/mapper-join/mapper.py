#!/usr/bin/env python

""" Reads the flights and airlines datasets and generates a join in the mapper side"""

import sys
import os

# flights.csv fields
# YEAR
# MONTH
# DAY
# DAY_OF_WEEK
# AIRLINE
# FLIGHT_NUMBER
# TAIL_NUMBER
# ORIGIN_AIRPORT
# DESTINATION_AIRPORT
# SCHEDULED_DEPARTURE
# DEPARTURE_TIME
# DEPARTURE_DELAY
# TAXI_OUT
# WHEELS_OFF
# SCHEDULED_TIME
# ELAPSED_TIME
# AIR_TIME
# DISTANCE
# WHEELS_ON
# TAXI_IN
# SCHEDULED_ARRIVAL
# ARRIVAL_TIME
# ARRIVAL_DELAY
# DIVERTED
# CANCELLED
# CANCELLATION_REASON
# AIR_SYSTEM_DELAY
# SECURITY_DELAY
# AIRLINE_DELAY
# LATE_AIRCRAFT_DELAY
# WEATHER_DELAY


# airlines.csv fields
# IATA_CODE
# AIRLINE


separator = ','
airlines_filename = 'airlines.csv'
airlines = None
flights = []

if os.path.exists(airlines_filename):
    print("file exists")
else:
    raise Exception("file does not exist")

# read airlines file locally
airlines = {}
list_file = open(airlines_filename)
list_dm = set(l.strip() for l in list_file)
list_file.close()
for a in list_dm:
    a_splits = a.split(separator)
    airline_id = a_splits[0]
    airline_name = a_splits[1]
    airlines[airline_id] = airline_name

# read flights from STDIN
for line in sys.stdin:

    a_splits = line.strip().split(separator)
    flight_airline_id = a_splits[4]
    flight_number = a_splits[5]

    # join flight with airlines
    flight_airline_name = airlines.get(flight_airline_id)
    print("{}\t{}\t{}".format(flight_airline_id, flight_airline_name, flight_number))
