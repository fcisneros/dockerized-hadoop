#!/usr/bin/env python

"""Just count each tuple from mapper and emit each count (sort of groupby)"""

import sys
from collections import Counter


# input comes from STDIN
counts = Counter()
for line in sys.stdin:
    line = line.strip()

    # parse the input we got from mapper.py
    try:
        airline_id, airline_name, flight_number = line.split('\t')
        counts.update([(airline_id, airline_name, flight_number)])
    except ValueError:
        # ignore/discard this line
        continue

for c in counts.most_common():
    # airline_id, airline_name, flight_number, count
    print('{}\t{}\t{}\t{}'.format(c[0][0], c[0][1], c[0][2], c[1]))
