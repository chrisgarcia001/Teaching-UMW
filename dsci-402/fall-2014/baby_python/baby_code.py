def add_2(x, y, mult=1):
	val = x + y
	return val * mult

def all_nums(a, b, *nums):
	print(a)
	print(b)
	print(nums)

def unique_count(items):
# Sample Input: items = [1,1,1,2,2,2,2,3]
# Sample Output: {1:3, 2:4, 3:1}	
	h = {}
	for item in items:
		if h.has_key(item):
			h[item] += 1
		else:
			h[item] = 1
	return h

