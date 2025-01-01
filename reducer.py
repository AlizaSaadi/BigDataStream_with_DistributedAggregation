#!/usr/bin/env python

import sys

total_price = 0
count = 0

for line in sys.stdin:
    value = line.strip().split()
    
    total_price += float(value)
    count += 1

average_price = total_price / count if count > 0 else 0

print(f'average : {average_price}')

