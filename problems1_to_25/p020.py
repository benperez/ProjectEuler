from math import factorial
import time

if __name__ == "__main__":
	start = time.time()
	n = sum( (int(d) for d in str(factorial(100L)) ) )
	elapsed = time.time() - start
	print "found %d after %f seconds" % (n, elapsed)