
from drivers import DriverStore
from cars import CarStore
from dc_mapper import CarDriverMap

driver_store = DriverStore()
car_store = CarStore()
car_driver_map = CarDriverMap()

prompt = """\
\n1. Driver Management
2. Car Management
3. Assign a car to driver
4. Find car by driver id
5. Find driver by car id
6. Exit\n"""


while True:
	print(prompt)
	option = input('Select option: ').strip()
	if option == '1':
		driver_store.manager()
	elif option == '2':
		car_store.manager()
	elif option == '3':
		car_driver_map.assign_car_to_driver(car_store, driver_store)
	elif option == '4':
		car_driver_map.find_car_by_driver();
	elif option == '5':
		car_driver_map.find_driver_by_car();
	elif option == '6':
		break
	else:
		print('Invalid input! Try again')

	input('\n\nPress [Enter] to go back to main menu')



