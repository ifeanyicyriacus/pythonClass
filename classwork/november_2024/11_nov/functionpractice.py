def get_cube(number):
	if type(number) in [int, float]:
		return round(number ** 3, 3)
	raise TypeError
