"""
What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

from time import time

def fibonacci_generator():
	a,b = 1, 1
	while True:
		yield a
		a, b = b, a + b

if __name__ == "__main__":
	start = time()
	f = fibonacci_generator()
	i = 1
	while True:
		current = f.next()
		if len(str(current)) == 1000:
			break
		i += 1
	answer = i
	elapsed = time() - start
	print "found %s after %s seconds" % (answer, elapsed)