def boolean_for_even_or_odd(numbers:list) -> int:
    return [(x % 2 == 0) for x in numbers]
	#return [True if (x % 2 == 0) else False for x in numbers]
    
