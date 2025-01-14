import math

def parse_even_digit(text:str) -> list:
    result = []
    for element in text:
        if element.isdigit():
            if int(element) % 2 == 0:
                result.append(int(element))
    return result

def number_to_square_dict(number:int) -> dict:
    dictionary = {1: number, 2: math.pow(number, 2)}
    return dictionary