#!/usr/bin/env python

"""Just count each tuple from mapper and emit each count (sort of groupby)"""

import sys
from collections import Counter


counts = Counter()
airlines = {}

for line in sys.stdin:
    line = line.strip()
    airline_id, flight_number, airline_name = line.split("\t")

    if airline_id != '-' and airline_name != '-':
        airlines[airline_id] = airline_name
    elif airline_id != '-' and flight_number != '-':
        counts.update([(airline_id, flight_number)])


# Emit results
for c in counts.most_common():
    # airline_id, airline_name, flight_number, count
    a_id = c[0][0]
    f_number = c[0][1]
    a_name = airlines.get(a_id)
    count = c[1]
    print('{}\t{}\t{}\t{}'.format(a_id, a_name, f_number, count))


