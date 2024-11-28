def sum_of_even_number(numbers:list) -> int:
	return sum([1 if (x % 2 == 0) else 0 for x in numbers])
    #return sum([1 for x in [1,5,7,3,2,9,8,10] if (x % 2 == 0)])
    #return len([x for x in [1,5,7,3,2,9,8,10] if (x % 2 == 0)])
    
    
