def odd_even_count(numbers:list) -> list:
    result = [0, 0]
    for number in numbers:
        if number % 2 == 0:
            result[1] += 1
        else:
            result[0] += 1
    return result
    
