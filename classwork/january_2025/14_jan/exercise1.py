import math

def parse_even_digit(text:str) -> list:
    return [x for x in list([int(x) for x in text if x.isdigit()]) if x % 2 == 0]

def number_to_square_dict(number:int) -> dict:
    dictionary = {1: number, 2: math.pow(number, 2)}
    return dictionary

def filter_between_20_and_50(numbers:list) -> list:
    return list(filter(lambda number: 20 <= number <= 50, numbers))