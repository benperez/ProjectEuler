import time

primes = [2]

def gen_primes():
	yield 2
	i = 3
	while True:
		for prime in primes:
			if i % prime == 0 or prime * prime > i:
				break
		if i % prime:
			primes.append(i)
			yield i
		i += 2

if __name__ == "__main__":
	while True:
		n = int(raw_input('Give amount: '))
		start = time.time()
		pgen = gen_primes()
		lastprime = 0
		for i in range(0,n):
			lastprime = pgen.next()
		elapsed = (time.time() - start)
		print "Found %d after %s seconds" % (lastprime, elapsed)