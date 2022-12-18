#!/usr/bin/env python3
import sys

ci = 0
mi = 0.0
vi = 0.0

for line in sys.stdin:
	cort = line.rstrip().split(':')
	ck = int(cort[0])
	vk = float(cort[1])
	mk = float(cort[2])
	
	vi = (ci * vi + ck * vk) / (ci + ck) + ci * ck * ((mi - mk) / (ci 
+ ck)) ** 2
	mi = (ci * mi + ck * mk) / (ci + ck) 
	ci += ck

print(str(vi))

