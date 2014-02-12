"""
Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

from time import time
from itertools import count
from heapq import heappush, heappop

# Generator that yields i^2 + 2*i, i^2 + 4*i, i^2 + 6*i, ..., etc.
# This stream of multiples is used to weed out non-primes
def composite_chain(seed):
	# can start checking for composites at seed^2
	# composites less than this will already have been generated
	current = seed * seed + 2 * seed
	while True:
		yield current
		current = current + 2 * seed

# An incremental version of the Sieve of Eratosthenes
def primes():
	yield 2
	yield 3
	# composites are stored in a min-heap. Smaller composites
	# need to be accessed first
	composite_heap = [ (9, composite_chain(3) ) ]
	# Iterate indefinitely over all odd numbers
	for n in count(5,2):
		# n is a composite number and is therefore not prime
		if n == composite_heap[0][0]:
			# PopPush/Increment all duplicate composites on the heap
			while n == composite_heap[0][0]:
				smallest_comp, comp_chain = heappop(composite_heap)
				heappush(composite_heap, (comp_chain.next(), comp_chain) )
		# n is not a composite and therefore is prime
		else:
			yield n
			# add n^2 and n's future multiples to the heap
			heappush(composite_heap, (n**2, composite_chain(n)) )

# prime_tracker holds: [greatest prime generated, prime generator, set of primes generated]
def is_prime(n, prime_tracker):
	# dynamically generate more primes as needed
	while n > prime_tracker[0]:
		prime_tracker[0] = prime_tracker[1].next()
		prime_tracker[2].add(prime_tracker[0])
	return n in prime_tracker[2]

def quadratic_formula(a,b):
	for n in count():
		yield pow(n,2) + a * n + b

def count_consecutive_primes(a, b, prime_tracker):
	# count the number of consecutive primes
	n_consecutive_primes = 0
	for n in quadratic_formula(a,b):
		if is_prime(n, prime_tracker):
			n_consecutive_primes = n_consecutive_primes + 1
		else:
			return n_consecutive_primes

if __name__ == "__main__":
	start = time()
	# do a grid search on -1000 < a < 1000, -1000 < b < 1000 to find the max length chain
	prime_tracker = [0, primes(), set()]
	max_chain_length, a_max, b_max = -1, -1000, -1000
	for a in xrange(-999, 1000):
		for b in xrange(-999, 1000):
			chain_length = count_consecutive_primes(a, b, prime_tracker)
			if chain_length > max_chain_length:
				max_chain_length, a_max, b_max = chain_length, a, b
	elapsed = time() - start
	print "Found %s after %s seconds" % (a_max * b_max, elapsed)