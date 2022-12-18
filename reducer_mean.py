#!/usr/bin/env python3
import sys

ci = 0.0
mi = 0

for line in sys.stdin:
	key_value = line.rstrip().split(':')
	ck = int(key_value[0])
	mk = float(key_value[1])
	
	mi = (ci * mi + ck * mk) / (ci + ck) 
	ci += ck

print(str(mi))

