def sum_of_even(numbers:list) -> int:
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total

