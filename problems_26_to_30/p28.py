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
import pdb

if __name__ == "__main__":
    start = time()
    spiral_sum, corners, period, current, max_value = 0, 4, 2, 1, 1001 * 1001
    # pdb.set_trace()
    while current <= max_value:
        # add in the next corner number of the spiral sum
        spiral_sum = spiral_sum + current
        # find the next corner number of the spiral sum
        if corners > 0:
            corners = corners - 1
        else:
            # jumping to a new, wider layer
            corners = 3
            period = period + 2
        current = current + period
    elapsed = time() - start
    print "Found %s after %s seconds" % (spiral_sum, elapsed)