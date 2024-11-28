def uzo() -> list:
	return [x for x in range(1, 6)]

def get_cube(numbers) -> list:
	return [x**3 for x in numbers]

print(get_cube(uzo()))



print([i for i in num if i%2 == 0])

print([1 if (i%2 == 0) else 0 for i in num])


