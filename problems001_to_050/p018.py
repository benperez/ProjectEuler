import time
from sys import maxint
input_string = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

# parse the input and build an array of indices
input = [ int(n) for line in input_string.split('\n') for n in line.split() ]
# generate a topological ordering of nodes
t_orderings, current = [], 0
while current * (current + 1) / 2 <= len(input):
	t_orderings.extend( [(current, offset) for offset in xrange(0,current)] )
	current = current + 1

#returns the children of the node in the given index
def child(index):
	t_order, offset = t_orderings[index]
	first_child = t_order * (t_order + 1) / 2 + offset
	return first_child

if __name__ == "__main__":
	start = time.time()
	# consider the nodes in topological order
	cost = [-1 * maxint for i in input]
	cost[0] = input[0]
	for idx in xrange(0,len(input)):
		child_idx = child(idx)
		if child_idx >= len(input):
			break
		cost[child_idx] = max(cost[child_idx], cost[idx] + input[child_idx])
		cost[child_idx+1] = max(cost[child_idx+1], cost[idx] + input[child_idx+1])
	max_path_sum = max(cost)
	elapsed = time.time() - start
	print "found %d after %f seconds" % (max_path_sum, elapsed)