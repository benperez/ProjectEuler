"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

from itertools import ifilter
from time import time

def timed(func):
	def wrapper(*args, **kwargs):
		start = time()
		result = func(*args,**kwargs)
		elapsed = time() - start
		print "%s found %s after %s seconds" % (func.func_name, result, elapsed)
		return result

	return wrapper

@timed
def imperative():
	digit_fifths = set()
	for i in xrange(2,236196):
		if i == sum( [ pow(int(c), 5) for c in str(i) ] ):
			digit_fifths.add(i)
	return sum(digit_fifths)

@timed
def functional():
	digit_powers = lambda n: sum( pow(int(c), 5) for c in str(n) ) == n
	return sum(ifilter(digit_powers, xrange(2,236196)))

if __name__ == "__main__":
	functional()
	imperative()