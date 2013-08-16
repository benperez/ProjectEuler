primes = [2]

def gen_primes(n):
	yield 2
	for i in range(3,n+1,2):
		for prime in primes:
			if i % prime == 0 or prime * prime > i: break
		if i % prime:
			primes.append(i)
			yield i

def primeFactors(n):
	for prime in gen_primes(n):
		while n % prime == 0:
			n = n / prime
			yield prime
		if n == 1:
			break

if __name__ == "__main__":
	while True:
		n = int(raw_input('Give amount: '))
		i = 2
		while i * i < n:
			while n % i == 0:
				n = n / i
			i = i + 1
		print n