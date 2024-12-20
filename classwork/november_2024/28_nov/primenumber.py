def is_prime(number:int) -> list:

    for value in range(2, number):
        if number % value == 0:
            return False
    return True

def get_prime_numbers(number:int) -> list:
    return [value for value in range(2, number) if is_prime(value)]

    
    
    #use all function


