def get_summation(args:list = [])-> float:
    sum = 0.0
    for number in args:
        sum += number
    return round(sum, 2)
    
