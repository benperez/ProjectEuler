"""
Problem 6:
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import time

if __name__ == "__main__":
	start = time.time()
	n = 100
	diff = 1.0/4.0*pow(n,4) + 1.0/6.0*pow(n,3) - 1.0/4.0*pow(n,2) - 1.0/6.0*n
	elapsed = (time.time() - start)
	print "Found %d in %s seconds" % (diff, elapsed)
