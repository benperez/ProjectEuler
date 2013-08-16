import time

if __name__ == "__main__":
	start = time.time()
	n = 100
	diff = 1.0/4.0*pow(n,4) + 1.0/6.0*pow(n,3) - 1.0/4.0*pow(n,2) - 1.0/6.0*n
	elapsed = (time.time() - start)
	print "Found %d in %s seconds" % (diff, elapsed)