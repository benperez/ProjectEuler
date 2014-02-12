from time import time

def cycle_length(d):
	seen_remainders = {}
	n = 10
	steps = 1
	while True:
		p, r = divmod(n,d)
		if r == 0:
			return steps
		elif r in seen_remainders:
			return steps - seen_remainders[r]
		else:
			seen_remainders[r] = steps
			n = r * 10
			steps = steps + 1

if __name__ == "__main__":
	start = time()
	answer, max_len = 0, 0
	for d in xrange(1,1000):
		l = cycle_length(d)
		if l > max_len:
			max_len = l
			answer = d
	elapsed = time() - start
	print "Found %s after %s seconds" % (answer, elapsed)