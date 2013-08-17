"""
Problem 14:
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import time

def collatz(n):
	while n > 1:
		yield n
		n = n / 2 if n % 2 == 0 else 3 * n + 1
	yield 1

def len_collatz(n):
	l = 1
	while n > 1:
		n = n / 2 if n % 2 == 0 else 3 * n + 1
		l += 1
	return l

if __name__ == "__main__":
	while True:
		n_iterations = int(raw_input("Largest Number to Try:"))
		if n_iterations == 0:
			break
		start = time.time()
		longest_collatz_sequence = 0
		longest_starting_number = 0
		for i in range(1,n_iterations+1):
			l_i = len_collatz(i)
			if l_i > longest_collatz_sequence:
				longest_collatz_sequence = l_i
				longest_starting_number = i
		elapsed = (time.time() - start)
		print "Found %s of length %s after %s seconds" % (longest_starting_number, longest_collatz_sequence, elapsed)