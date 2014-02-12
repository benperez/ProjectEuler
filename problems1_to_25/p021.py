"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a not eqal b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from time import time
from math import sqrt

def divisor_sum(n):
	if n == 1:
		return 0
	if 1 < n < 4:
		return 1
	running_sum = 1
	root = int(sqrt(n))
	for p in xrange(2, int(sqrt(n))):
		q, r = divmod(n, p)
		if r == 0:
			running_sum += p + q
	# sqrt is an edge case, only needs to be added once
	if n % root == 0:
		running_sum += root
	return running_sum

if __name__ == "__main__":
	max_number = 10000
	start = time()
	sums = [divisor_sum(i) for i in xrange(1, max_number)]
	amicable_sum = 0
	for i in xrange(0, max_number - 1):
		opposite = sums[i]
		if opposite == i + 1:
			continue
		if opposite < max_number and sums[opposite-1] == i + 1:
			amicable_sum += i + 1
	elapsed = time() - start
	print "found %s after %s seconds" % (amicable_sum, elapsed)