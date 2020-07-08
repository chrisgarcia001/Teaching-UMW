# Compute factorial
def fac(n):
	if n == 0:
		return 1
	else:
		return n * fac(n - 1)

# Recursively reverse a list
def rrev(elements):
	if len(elements) == 0:
		return []
	else:
		return rrev(elements[1:]) + [elements[0]]

# Slow Fibonacci sequences
def fib(f, s, n):
	if n == 1:
		return f
	elif n == 2:
		return s
	else:
		return fib(f, s, n - 1) + fib(f, s, n - 2) 
		
# Fast Fibonacci sequences using dynamic programming.
def ffib(f, s, n, cache = {}):
	if cache.has_key(n):
		return cache[n]
	elif n == 1:
		return f
	elif n == 2:
		return s
	else:
		cache[n] = ffib(f, s, n - 1, cache) + ffib(f, s, n - 2, cache)
		return cache[n]
		
# Flatten a list of lists
# Example: flatten([[[1,2],3], [4,5,6], [[[7,8],9]]]) = [1,2,3,4,5,6,7,8,9]
def flatten(elts):
	if elts == []:
		return []
	elif type(elts[0]) == type([]):
		return flatten(elts[0]) + flatten(elts[1:])
	else:
		return [elts[0]] + flatten(elts[1:])
