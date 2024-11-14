def get_product(number_a, number_b = 1):    
    product = 0
    if type(number_a) in [int, float] and type(number_b) == int:    
        for _ in range(abs(number_b)):
            if number_a < 0 and number_b >= 0:
                product -= abs(number_a)
            elif number_a >= 0 and number_b < 0:
                product -= number_a
            else:
                product += abs(number_a)
        return product
    elif type(number_a) in [int, float] and type(number_b) == float:
        
        whole = str.split(str(abs(number_b)), ".")[0]
        decimal = str.split(str(abs(number_b)), ".")[1]
        decimal_point = len(decimal)
        whole_decimal = int(whole + decimal)

        for _ in range(whole_decimal):
            if number_a < 0 and number_b >= 0:
                product -= abs(number_a)
            elif number_a >= 0 and number_b < 0:
                product -= number_a
            else:
                product += abs(number_a)
                
        for _ in range(decimal_point):
            product /= 10.0
        return round(product, 2)
        
        
    raise TypeError    
