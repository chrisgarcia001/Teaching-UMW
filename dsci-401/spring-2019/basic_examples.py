from functools import reduce

# Some basic illustrations of Python concepts.

# Illustrates optional/default args
def print_all(a, b, c=1, d=2):
	print(a)
	print(b)
	print(c)
	print(d)
	
#Illustrates optional/unbounded args
def print_optional(a, b, *c):
	print(a)
	print(b)
	print(c)
	
# Compute the nth Fibonacci number for arbitrary first and second elements.
def fib(a, b, n, cache={}):
	if n in cache:
		return cache[n]
	if n == 1:
		return a
	if n == 2:
		return b
	else:
		cache[n] = fib(a, b, n - 1, cache) + fib(a, b, n - 2, cache)
		return cache[n]

# Compute the cartesian product on the given sets (lists).
def cartesian_prod(*lists):
	if len(lists) == 1:
		return [[x] for x in lists[0]]
	else:
		rest = cartesian_prod(*lists[1:])
		return reduce(lambda x,y: x + y, [[[i] + j for j in rest] for i in lists[0]]) # functional way
		
		# Manual/loop-based way:
		# cp = []
		# for i in lists[0]:
			# for j in rest:
				# cp.append([i] + j)
		# return cp		
		
# Generate all unique combinations of elements, taken k at a time.
def gen_combs(elems, k):
	if k == len(elems):
		return [elems]
	if k == 1:
		return [[x] for x in elems]
	else:
		return [[elems[0]] + c for c in gen_combs(elems[1:], k - 1)] + gen_combs(elems[1:], k)
