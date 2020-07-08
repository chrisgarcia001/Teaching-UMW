from vehicles import *

v1 = Vehicle("hannah", 4)
v2 = Vehicle("alex", 2, location = (3,5), direction = (1, 4), owner = "Alex")

v1.print_info()
print("\n")
v2.print_info()
v2.set_direction(3, 5)
v2.location = (20, 20)  # Inconsistent way to change attribute - not good
print("\n---Alex after change: \n")
v2.print_info()
v2.base_move(1500)
v2.print_info()

c1 = Car("Ruth", 4, location = (3,5), direction = (1, 4), owner = "Ruth", 
         fuel_capacity = 20, mpg = 50, fuel_level = 15)
c1.print_info()

# One way to check distance - using exception handling
c1.fuel_level = 15
distance = 10000
try:
	c1.move(distance)
except ValueError as err:
	print("Distance too far, changing to " + str(c1.max_dist()))
	c1.move(c1.max_dist())

# Another way to check - using built-in methods of Car class.	
c1.fuel_level = 15
distance = 10000
if c1.max_dist() < distance: 	
	print("Adjusting distance to: " + str(c1.max_dist()))
	distance = c1.max_dist()
c1.move(distance)


