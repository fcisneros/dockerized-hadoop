#!/usr/bin/env python

""" Reads the flights and airlines datasets and generates a join in the mapper side"""

import sys
from collections import Counter

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
airlines = {}
flights = []

for line in sys.stdin:
    splits = line.strip().split(separator)
    if len(splits) == 2:  # airlines dataset
        airline_id = splits[0]
        airline_name = splits[1]
        airlines[airline_id] = airline_name
    else:
        airline_id = splits[4]
        flight_number = splits[5]
        flights.append((airline_id, flight_number))


# Let's join both lists ane emit tuples
for f in flights:
    airline_name = airlines.get(f[0])
    if airline_name:
        print("{}\t{}\t{}".format(f[0], airline_name, f[1]))
