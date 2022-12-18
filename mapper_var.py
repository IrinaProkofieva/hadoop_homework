#!/usr/bin/env python3
import sys
from csv import reader

chunk_size = 0
sum_val = 0
var_val = 0
mean_prev_chunk = 0

for row in reader(sys.stdin):
	if len(row) < 9:
		continue
	price = row[9]
	if price.isdigit():
		price = int(price)
		if chunk_size==0:
			var_val = 0
			mean_prev_chunk = price
		else:
			mean_prev_chunk = sum_val / chunk_size
			var_val = (var_val  * chunk_size) / (chunk_size + 
1) + chunk_size * ((price - mean_prev_chunk) / (chunk_size + 1))**2
		sum_val += price
		chunk_size += 1
if chunk_size > 0:
	mean_val = sum_val / chunk_size
	print('%s:%s:%s' % (str(chunk_size), str(var_val), str(mean_val)))

