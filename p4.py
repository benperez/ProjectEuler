import time

def listPalindromes():
	return [i*100000 + j*10000 + k*1000 + k*100 + j*10 + i for i in range(9,0,-1) for j in range(9,-1,-1) for k in range(9,-1,-1)]

if __name__ == "__main__":
	start = time.time()
	palindromes = listPalindromes()
	maxpal = 0
	for i in range(100,1000):
		for j in range(100,1000):
			curr = i*j
			if curr > maxpal and curr in palindromes:
				maxpal = curr
	elapsed = (time.time() - start)
	print "Largest palindrome is %s, found in %s seconds" % (maxpal, elapsed)