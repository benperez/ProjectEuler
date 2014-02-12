"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from time import time
from collections import deque

if __name__ == "__main__":
	start = time()
	# generate all the permutations
	queue = deque()
	queue.append(  ('', [str(n) for n in xrange(10)]) )
	yielded = 0
	final_permutation = ''
	while queue:
		current_sequence, remaining = queue.popleft()
		if not remaining:
			if yielded == 999999:
				final_permutation = current_sequence
				break
			else:
				yielded += 1
		for i in xrange(len(remaining)):
			next = remaining[i]
			# copy the old list over
			next_list = list(remaining)
			del next_list[i]
			queue.append( (current_sequence + next, next_list) )
	answer = final_permutation
	elapsed = time() - start
	print "found %s after %s seconds" % (answer,elapsed)