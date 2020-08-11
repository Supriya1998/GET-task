
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

class Driver:	
	d_id_cur = 1000
		
	def __init__(self):
		self.d_id = str(Driver.d_id_cur + 1) # d_id's start from 1001, ...
		Driver.d_id_cur += 1
		print('### Insert Details ###')
		self.name = input('Name: ').strip()
		self.age = input('Age: ').strip()
		self.license_no = input('License number: ').strip()

	def print_driver_details(self):
		print('Driver ID:', self.d_id)
		print('Name:', self.name)
		print('Age:', self.age)
		print('License number:', self.license_no)
	
	def update_shift_details(self):
		#if hasattr(self, 'shift'):
			#print('Shift details already available for driver "' + self.d_id + '". Overwrite? (y/n): ')
			#return
			
		self.shift = {}
		for day in days:
			while True:
				user_input = input("Working on " + day + ": (y/n) ").strip()
				if user_input.lower() == 'n':
					self.shift[day] = 'Not working'
					break
				elif user_input.lower() == 'y':
					self.shift[day] = {}
					self.shift[day]['from'] = input('Working on ' + day + ' from (e.g., 2pm): ').strip()
					self.shift[day]['until'] = input('Working on ' + day + ' until (e.g., 10pm): ').strip()
					break
				else:
					print('Invalid input! Enter "y" or "n"')
		
	
	def show_shift_details(self):
		if hasattr(self, 'shift') == False:
			print('Shift details are not available for driver "' + self.d_id + '"')
			return
	
		print('Shift details for "' + self.d_id + '" are as follows:-')
		
		for day in days:
			if type(self.shift[day]) is dict:
				print(day + ': ' + 'From ' + self.shift[day]['from'] + \
						' until ' + self.shift[day]['until'])
			else:
				print(day + ': ' + self.shift[day])

class DriverStore:

	def __init__(self):
		self.drivers = []
	
	def add_driver(self):
		driver = Driver()
		self.drivers.append(driver)
		print('Driver added successfully! Assigned driver ID:', driver.d_id)
	
	def find_driver_by_id(self, prompt_string):
		input_id = input(prompt_string).strip()
		for driver in self.drivers:
			if driver.d_id == input_id:
				return driver
		print('No driver with driver_id = "' + input_id + '" found.')
		return None

	
	def show_driver_by_id(self):	
		result = self.find_driver_by_id('Insert driver id: ')
		if result == None:
			return
		
		print('\n\nDetails for driver with id:', result.d_id)
		result.print_driver_details()


	def show_all_drivers(self):
		if len(self.drivers) == 0:
			print('No driver entries added yet! Add some to make this feature useful ;)')		
			return
			
		for driver in self.drivers:
			print('----------------------')
			driver.print_driver_details()


	def insert_shift_details_for_driver(self):
		result = self.find_driver_by_id('Enter driver id for whom shift details are to be entered: ')		
		if result == None:
			return
		result.update_shift_details()
		
	
	def show_shift_details_for_driver(self):
		result = self.find_driver_by_id('Enter driver id for whom shift details are to be shown: ')		
		if result == None:
			return
		result.show_shift_details()
		
	
	def manager(self):
		prompt = """\
\n1. Add driver
2. Add shift details for a driver
3. Show shift details for a driver
4. Show driver by driver ID
5. Show all drivers
6. Exit driver management menu\n"""

		while True:
			print(prompt)
			option = input('Select option: ').strip()
			if option == '1':
				self.add_driver()
			elif option == '2':
				self.insert_shift_details_for_driver()
			elif option == '3':
				self.show_shift_details_for_driver()
			elif option == '4':
				self.show_driver_by_id()
			elif option == '5':
				self.show_all_drivers()
			elif option == '6':
				break
			else:
				print('Invalid option! Try again')
		
			input('\n\nPress [Enter] to go back to driver management menu ')

#Test run
#DriverStore().manager()





