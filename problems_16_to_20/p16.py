"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""

import time

if __name__ == "__main__":
	start = time.time()
	#Most number systems are clever and will represent powers of 2 perfectly
	digit_sum = sum((int(x) for x in str(pow(2,1000))))
	elapsed = (time.time() - start)
	print "found %s in %s seconds" % (digit_sum, elapsed)