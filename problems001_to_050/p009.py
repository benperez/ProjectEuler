"""
Problem 9:
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import time
from math import sqrt,floor

if __name__ == "__main__":
	start = time.time()
	for a in range(1,333):
		for b in range(a+1, (1000 - a) / 2 + 1):
			c = 1000 - a - b
			if c == sqrt(a*a + b*b):
				elapsed = (time.time() - start)
				print "Found %s after %s seconds" % (a*b*c,elapsed)
	
