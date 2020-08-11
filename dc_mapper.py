

class CarDriverMap:
	
	def __init__(self):
		self.car_driver_mapping = {} # (key, value) : (car_id, driver_id)

	def assign_car_to_driver(self, car_store, driver_store):
		car = car_store.find_car_by_id('Enter Car ID of the car which is to be assigned a driver: ')
		if car == None:
			return
		
		if car.c_id in self.car_driver_mapping.keys():
			print('Car already assigned to some driver! Try some other car')
			return

		driver = driver_store.find_driver_by_id('Enter driver ID of the driver to whom the car "' \
													+ car.c_id + '" is to be assigned: ')		
		if driver == None:
			return

		if driver.d_id in self.car_driver_mapping.values():
			print('Driver already assigned to some car! Try some other driver')
			return

		self.car_driver_mapping[car.c_id] = driver.d_id
		print('The car "' + car.c_id + '" is assigned to driver "' \
				+ driver.d_id + '" successfully!')


	def find_car_by_driver(self): # just find if this driver is assigned to some car	
		driver_id_input = input('Enter driver ID of the driver whose car is to be found: ').strip()
			
		if driver_id_input not in self.car_driver_mapping.values():
			print('This driver isn\'t assigned any car.')
			return
	
		for car_id, driver_id in self.car_driver_mapping.items():
			if driver_id == driver_id_input:
				print('The driver "' + driver_id + '" is assigned car "' + car_id + '"')
				return

	def find_driver_by_car(self):
		car_id_input = input('Enter car ID of the car whose driver is to be found: ').strip()
		
		if car_id_input not in self.car_driver_mapping.keys():
			print('This car isn\'t assigned to any driver.')
			return

		for car_id, driver_id in self.car_driver_mapping.items():
			if car_id == car_id_input:
				print('The car "' + car_id + '" is assigned to driver "' + driver_id + '"')
				return



