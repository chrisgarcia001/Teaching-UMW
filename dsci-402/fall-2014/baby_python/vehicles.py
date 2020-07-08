class Vehicle:
	def __init__(self, name, speed, direction):
		self.name = name
		self.speed = speed
		self.direction = direction
	
	def print_info(self):
		print("Vehicle Info:")
		print("  Name: " + str(self.name))
		print("  Speed: " + str(self.speed))
		print("  Direction: " + str(self.direction))
		
	def xyz(self):
		print("XYZ!")
		
class Car(Vehicle):
	def __init__(self, name, speed, direction, mpg, fuel_level = 0, mileage = 0):
		self.name = name
		self.speed = speed
		self.direction = direction
		self.mpg = mpg
		self.fuel_level = fuel_level
		self.mileage = mileage
		
	def drive(self, distance):
		self.fuel_level -= (float(distance) / float(self.mpg))
		self.mileage += distance
		self.speed = 0
		
	def fill_up(self, gallons):
		self.fuel_level += gallons
		
	def print_info(self):
		print("Vehicle Info:")
		print("  Name: " + str(self.name))
		print("  Speed: " + str(self.speed))
		print("  Direction: " + str(self.direction))
		print("  MPG: " + str(self.mpg))
		print("  Fuel Level: " + str(self.fuel_level))
		print("  Mileage: " + str(self.mileage))
		