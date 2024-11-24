from math import sqrt

def is_even(number : int) -> bool:
    return True if (number % 2 == 0) else False

def is_prime_number(number : int) -> bool:
    if number == 1:
        return false
    for test in range(2, number):
        if number % test == 0:
            return False
    return True

def subtract(number_1:int, number_2:int) -> int:
    return abs(number_1 - number_2)

def divide(number_1:int, number_2:int) -> float:
    if number_2 == 0: return float(0)
    quotient = float(number_1/number_2)
    return quotient
    
def factor_of(number : int) -> int:
    factor_count = 1
    for test in range(1, number):
        if number % test == 0:
            factor_count += 1
    return factor_count
    
def is_square(number : int) -> bool:
    number_sqrt = sqrt(number)
    number_sqrt_int = int(number_sqrt)
    if number_sqrt_int == number_sqrt:
        return True
    else:
        return False

def is_palindrome(number : int) -> bool:
    number_str = str(number)
    if number_str == number_str[::-1]:
        return True
    else:
        return False

def factorial_of(number : int) -> int:
    if number == 1: return 1
    return number * factorial_of(number - 1)


def square_of(number : int) -> int:
    return number * number




