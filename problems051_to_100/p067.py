import time

# parse the input and build an array of indices
input = [ int(n) for line in open('data/triangle.txt') for n in line.split() ]
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
	cost = [-1 for i in input]
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