# Get the Cartesian product of multiple sets.
def cart_product(*sets):
	if len(sets) == 0:
		return []
	elif len(sets) == 1:
		return map(lambda x: [x], sets[0])
	else:
		rest = cart_product(*(sets[1:]))
		fn = lambda x: map(lambda y: [x] + y, rest)
		return reduce(lambda x, y: x + y, map(fn, sets[0]))

# Get every combination of n elements drawn from items.		
# **NOTE: Assumes len(items) >= n.
def ncombs(items, n):
	if n == 1:
		return map(lambda x: [x], items)
	elif len(items) == n:
		return [items]
	else:
		next_reduct = ncombs(items[1:], n - 1)
		add = lambda comb: [items[0]] + comb
		return map(add, next_reduct) + ncombs(items[1:], n)

# Takes a new item and list of items and makes list of lists with 
# the new item in each position added to the old list.
# Ex: all_interleaves('a', [1,2,3]) = [['a',1,2,3],[1,'a',2,3'],[1,2,'a',3],[1,2,3,'a']]
def all_interleaves(new_item, items):
	ints = []
	for i in range(len(items) + 1):
		nxt = list(items)
		nxt.insert(i, new_item)
		ints.append(nxt)
	return ints	
	
# Generates all permutations for a list of items.
# Ex: all_perms([1,2,3]) = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
def all_perms(items):		
	if len(items) == 1:
		return [items]
	else:
		subs = all_perms(items[1:])
		return reduce(lambda x,y: x+y, map(lambda z: all_interleaves(items[0], z), subs))

# Get the powerset (i.e. set of all possible subsets) for the items.
# Ex: powerset([1,2,3]) = [[1, 2, 3], [1, 2], [1, 3], [1], 
#                          [2, 3], [2], [3], []]		
def powerset(items):
	if len(items) == 0:
		return [[]]
	else:
		subs = powerset(items[1:])
		return map(lambda x: [items[0]] + x, subs) + subs

	
			