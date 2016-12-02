class Car(object):
	
	def __init__(self, name = "General", model = "GM" , car_type = None):
		self.speed = 0
		self.car_type = car_type
		self.num_of_doors = 4 if not(name =='Porshe' or name == 'Koenigsegg') else 2
		self.num_of_wheels = 8 if car_type == "trailer" else 4
		self.name = name
		self.model = model
	
	def is_saloon(self):
		if self.car_type != "trailer":
			self.car_type = "saloon"
			return True
		return False

	def drive(self, moving_speed):
		if moving_speed == 3:
			self.speed = 1000
		elif moving_speed == 7:
			self.speed = 77
		return self
