def multiple_of_3_between(num1:int, num2:int) -> list:
    #return [x for x in range(num1, num2+1) if (x % 3 == 0)]
    return [x for x in range(num1, num2 + 1, 3)]
    
    #I am having issue with redundant conditions
