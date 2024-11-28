def square_odds(numbers:list) -> list:
    return [x ** 2 for x in numbers if x % 2 == 1]
