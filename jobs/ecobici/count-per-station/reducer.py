#!/usr/bin/env python

"""Calculates the sum of records per station"""

import sys


current_station = None
current_count = 0
station = None

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()

    # parse the input we got from mapper.py
    station, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        # ignore/discard this line
        continue

    # this only works because Hadoop sorts map output
    # by key (here: station) before it is passed to the reducer
    if current_station == station:
        current_count += count
    else:
        if current_station:
            # write result to STDOUT
            print('{}\t{}'.format(current_station, current_count))
        current_count = count
        current_station = station

# do not forget to output the last station
if current_station == station:
    print('{}\t{}'.format(current_station, current_count))

