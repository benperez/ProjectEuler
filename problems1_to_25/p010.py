"""
Problem 10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import time
from math import sqrt

primes = [2]

def gen_primes_less_than(n):
	yield 2
	for i in range(3,n,2):
		s = sqrt(i)
		for prime in primes:
			if i % prime == 0 or prime > s: break
		if i % prime:
			primes.append(i)
			yield i

if __name__ == "__main__":
	while True:
		n = int(raw_input('Give amount: '))
		if n == 0 :
			break
		start = time.time()
		prime_sum = sum(gen_primes_less_than(n))
		elapsed = (time.time() - start)
		print "Found %d after %s seconds" % (prime_sum, elapsed)
