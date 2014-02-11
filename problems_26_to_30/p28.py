"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

from time import time

if __name__ == "__main__":
    start = time()
    spiral_sum, corners, period, current, max_value = 1, 4, 3, 1, 5 * 5
    while current <= max_value:
        if corners > 0:
            spiral_sum = current
            corners = corners - 1
        else:
            corners = 4
            period = period + 2
        current = current + period
    elapsed = time() - start
    print "Found %s after %s seconds" % (spiral_sum, elapsed)