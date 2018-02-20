#!/usr/bin/env python

""" Reads the flights and airlines datasets and emits triplets that will be joined in the reducer """

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


def parse_airline(splitted):
    id = splitted[0]
    name = splitted[1]

    return id, name


def parse_flight(splitted):
    f_airline_id = splitted[4]
    f_number = splitted[5]

    return f_airline_id, f_number


# read inputs from STDIN
for line in sys.stdin:
    airline_id = ""
    airline_name = "-"
    flight_number = "-"

    splits = line.strip().split(separator)
    if len(splits) == 2:  # airlines data
        airline_id, airline_name = parse_airline(splits)
    else:
        airline_id, flight_number = parse_flight(splits)

    # emit triplet
    print("{}\t{}\t{}".format(airline_id, flight_number, airline_name))
