"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

from time import time

char_vals = { l: i for i, l in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1) }

if __name__ == "__main__":
	start = time()
	score_sum = 0
	with open('data/names.txt') as f:
		names = sorted(f.readline().replace('"','').split(','))
		score_sum = sum( ( sum( ( char_vals[l] for l in name ) ) * index for index, name in enumerate(names, 1) ) )
	elapsed = time() - start
	print "found %s after %s seconds" % (score_sum, elapsed)