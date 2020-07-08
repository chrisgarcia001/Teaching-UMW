
for item in range(101):
	print("Item: " + str(item))
	print("Item Again: " + str(item))
	
i = 0
ending = 100
while i <= ending:
	print("The value of i is: " + str(i))
	i = i + 1

if not(4 < 5) and (4 == 4):
	print("4 >= 5")
elif 4 == 5:
	print("4 == 5")
else:
	print("4 < 5")
	
def my_filter(criteria_f, elements): 
	# filter out all values e in elements for 
	# which criteria_f(e) == True
	return None
	
