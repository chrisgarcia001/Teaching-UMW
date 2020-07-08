import math

class Vehicle:
	def __init__(self, vid, capacity, location = (0, 0), 
				 direction = (0,0), owner = None):
		self.vid = vid
		self.capacity = capacity
		self.location = location
		self.direction = direction
		self.owner = owner

	def print_info(self):
		print("VID: " + str(self.vid))
		print("Capacity: " + str(self.capacity))
		print("Location: " + str(self.location))
		print("Direction: " + str(self.direction))
		print("Owner: " + str(self.owner))
		
	def set_direction(self, dx, dy):
		self.direction = (dx, dy)
		
	def base_move(self, distance):
		dx, dy = self.direction
		scale = distance / math.sqrt((dx ** 2) + (dy ** 2))
		x, y = self.location
		self.location = (x + (scale * dx), y + (scale * dy))
		return self.location
		
class Car(Vehicle):
	def __init__(self, vid, capacity, location = (0, 0), 
				 direction = (0,0), owner = None,
				 fuel_capacity = 15, mpg = 30.0, fuel_level = 10.0):
		# -----------------------------------------------------------
		# Something like this is the right way to do it -
		# Google it for exact details ;)
		#
		# super(Car, self).__init__(vid, capacity, location, 
		#						  direction, owner = None)
		# As mini-homework - figure out how to do it the right way.
		# -----------------------------------------------------------
		
		#------------------------------------------------------------
		# This is the wrong way:
		self.vid = vid
		self.capacity = capacity
		self.location = location
		self.direction = direction
		self.owner = owner
		#------------------------------------------------------------
		
		self.fuel_capacity = fuel_capacity
		self.mpg = mpg
		self.fuel_level = fuel_level
	
	def max_dist(self):	
		return self.fuel_level * self.mpg
		
	def move(self, distance):
		if distance > self.max_dist():
			# For more info - Google throwing/catching exceptions in Python
			raise ValueError("Distance beyond capacity")
		self.base_move(distance)
		burned = float(distance) / self.mpg
		print(" Old Fuel Level: " + str(self.fuel_level))
		self.fuel_level -= burned
		print(" New Fuel Level: " + str(self.fuel_level))
		
		
	