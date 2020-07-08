# Gets Cartesian Product for any number of sets.
def cart_prod(*sets):
	if len(sets) == 0:
		return []
	elif len(sets) == 1:
		return map(lambda x: [x], sets[0])
	else:
		rest = cart_prod(*sets[1:])
		fn = lambda x: map(lambda y: [x] + y, rest)
		return reduce(lambda x, y: x + y, map(fn, sets[0]))
		
# Get all combinations of length n.
def ncombs(items, n):
	if n == 1:
		return map(lambda x: [x], items)
	elif n == len(items):
		return [items]
	else:
		next_reduct = ncombs(items[1:], n - 1)
		return map(lambda x: [items[0]] + x, next_reduct) + ncombs(items[1:], n)

# Interleave item into all possible positions of elements and return the 
# resulting list.
def interleave_all(item, elements):
	ivs = []
	for i in range(0, len(elements) + 1):
		nxt = list(elements)
		nxt.insert(i, item)
		ivs.append(nxt)
	return ivs	
	
# Get all permutations possible from the items given.
def all_perms(items):
	if len(items) == 1:
		return [items]
	else:
		rest = all_perms(items[1:])
		return reduce(lambda x,y: x+y, map(lambda z: interleave_all(items[0], z), rest))
		