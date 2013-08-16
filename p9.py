import time
from math import sqrt,floor

if __name__ == "__main__":
	start = time.time()
	for a in range(1,333):
		for b in range(a+1, (1000 - a) / 2 + 1):
			c = 1000 - a - b
			if c == sqrt(a*a + b*b):
				elapsed = (time.time() - start)
				print "Found %s after %s seconds" % (a*b*c,elapsed)
	