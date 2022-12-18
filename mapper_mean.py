#!/usr/bin/env python3
import sys
from csv import reader

chunk_size = 0
sum_val = 0

for row in reader(sys.stdin):
	if len(row) < 9:
		continue
	price = row[9]
	if price.isdigit():
		price = int(price)
		sum_val += price
		chunk_size += 1

if chunk_size > 0:
	mean_val = sum_val / chunk_size
	print('%s:%s' % (str(chunk_size), str(mean_val)))
