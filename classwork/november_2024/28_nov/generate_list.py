def total(numbers:list) ->int:
    if len(numbers) == 0:
        return 0
    return numbers[0] + total(numbers[1:])

def generate_list():
	return total([x for x in range(1, 6)])

print(generate_list())

