import time

def gen_traingle_numbers():
	triangle, current_number = 1, 2
	while True:
		yield triangle
		triangle = triangle + current_number
		current_number += 1

def n_factors(n):
	i = 2
	while i * i < n:
		while n % i == 0:
			n = n / i
		i = i + 1

if __name__ == "__main__":
	start = time.time()
	for t in gen_traingle_numbers:
		
	elapsed = (time.time() - start)
	print "Found %d after %s seconds" % (max_product, elapsed)
