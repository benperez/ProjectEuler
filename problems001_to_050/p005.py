"""
Problem 5:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import time

if __name__ == "__main__":
	start = time.time()
	n = 1
	while True:
		if n%11==0 and n%12==0 and n%13==0 and n%14== 0 and n%15==0 and n%16==0 and n%17==0 and n%18==0 and n%19==0 and n%20==0:
			break
		n += 1
	print n
	elapsed = (time.time() - start)
	print "Found %s in %s seconds" % (n, elapsed)
