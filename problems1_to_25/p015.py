"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

import time

def pascal(n):
	pas = [[1],[1,1]]
	for i in xrange(2,n+1):
		pas.append([1])
		for j in xrange(0,i-1):
			pas[i].append(pas[i-1][j] + pas[i-1][j+1])
		pas[i].append(1)
	return pas

if __name__ == "__main__":
	pascals = pascal(20)
	#sum of squares of the nth row of pascals triangle is equal to the
	#middle number of the 2nth row
	print sum((x**2 for x in pascals[-1]))