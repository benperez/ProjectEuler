"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from time import time
from math import sqrt

def abundant(n):
	if n < 12:
		return False
	div_sum = 1
	for p in xrange(2, int(sqrt(n)) + 1):
		q, r = divmod(n, p)
		if r == 0:
			div_sum += p
			if p != q:
				div_sum += q
	return div_sum > n

if __name__ == "__main__":
	start = time()
	all_sum = sum(xrange(28124))
	abundant_numbers = [n for n in xrange(28124) if abundant(n)]
	abundant_set = set()
	abundant_sum = 0
	for i in xrange(len(abundant_numbers)):
		for j in xrange(len(abundant_numbers)):
			combination = abundant_numbers[i] + abundant_numbers[j]
			if combination > 28123:
				continue
			elif combination not in abundant_set:
				abundant_sum += combination
				abundant_set.add(combination)
	answer = all_sum - abundant_sum
	elapsed = time() - start
	print "found %s after %s seconds" % (answer,elapsed)