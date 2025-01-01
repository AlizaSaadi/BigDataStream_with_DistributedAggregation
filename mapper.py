#!/usr/bin/env python

import sys

for line in sys.stdin:
    price = float(line.strip())
    print(f'{price}')

