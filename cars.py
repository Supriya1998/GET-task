
class Car:
	c_id_cur = 3000
	
	def __init__(self):
		self.c_id = str(Car.c_id_cur + 1)
		Car.c_id_cur += 1
		print('### Insert Details ###')
		self.name = input('Car Name: ').strip()
		self.model = input('Car Model: ').strip()
		self.reg_no = input('Registration number: ').strip()

	
	def print_car_details(self):
		print('Car ID:', self.c_id)
		print('Car Name:', self.name)
		print('Car Model:', self.model)
		print('Registration number:', self.reg_no)
		
	
	def update_amenities(self):		
		if hasattr(self, 'amenities'):
			to_overwrite = input('Amenities data already exist for the given car." + \
					" Want to overwrite it? (y/n): ')
			if to_overwrite.lower() == 'n':
				return

		self.amenities = []
	
		print('Enter the car\'s amenities one by one')
		count = 1
		while True:
			self.amenities.append(input('Item ' + str(count) + ': '))
			want = ''
			while True:
				want = input('Want to add more items? (y/n): ')
				if want.lower() == 'y' or want.lower() == 'n':
					break
			if want.lower() == 'n':
				break
			count = count + 1


	def show_amenities(self):
		if hasattr(self, 'amenities') == False:
			print('Amenities are not available for car "' + self.c_id + '"')
			return

		print('The car\'s amenities are as follows:-')
		for count, item in enumerate(self.amenities):
			print(str(count + 1) + ". " + item)



class CarStore:
	
	def __init__(self):
		self.cars = []
	
	def add_car(self):
		car = Car()
		self.cars.append(car)
		print('Car added successfully! Assigned car ID:', car.c_id)

	def find_car_by_id(self, prompt_string):
		input_id = input(prompt_string).strip()
		for car in self.cars:
			if car.c_id == input_id:
				return car		
		print('No car with car_id = "' + input_id + '" found.')
		return None
	
	def show_car_by_id(self):
		result = self.find_car_by_id('Enter car id: ')
		if result == None:
			return
		print('\n\nDetails for car "' + result.c_id + '"')
		result.print_car_details()
	
	def show_all_cars(self):
		if len(self.cars) == 0:
			print('No car entries added yet! Add some to make this feature useful ;)')		
			return			
		for car in self.cars:
			print('----------------------')
			car.print_car_details()
	
	
	def update_amenities_for_car(self):
		result = self.find_car_by_id('Enter car id for which amenities are to be entered: ')
		if result == None:
			return
		result.update_amenities()	

	def show_amenities_for_car(self):
		result = self.find_car_by_id('Enter car id for which amenities are to be shown: ')
		if result == None:
			return
		result.show_amenities()	

	def manager(self):
		prompt = """\
\n1. Add car
2. Show car by car ID
3. Show all cars
4. Enter car's amenities
5. Show car's amenities
6. Exit car management menu\n"""

		while True:
			print(prompt)
			option = input('Select option: ').strip()
			if option == '1':
				self.add_car()
			elif option == '2':
				self.show_car_by_id()
			elif option == '3':
				self.show_all_cars()
			elif option == '4':
				self.update_amenities_for_car()
			elif option == '5':
				self.show_amenities_for_car()
			elif option == '6':
				break
			else:
				print('Invalid option! Try again')
		
			input('\n\nPress [Enter] to go back to car management menu ')

#Test run
#CarStore().manager()



