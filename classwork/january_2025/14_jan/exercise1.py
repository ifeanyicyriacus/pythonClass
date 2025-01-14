import math

def parse_even_digit(text:str) -> list:
    return [x for x in list([int(x) for x in text if x.isdigit()]) if x % 2 == 0]

def number_to_square_dict(number:int) -> dict:
    dictionary = {1: number, 2: math.pow(number, 2)}
    return dictionary

def filter_between_20_and_50(numbers:list) -> list:
    return list(filter(lambda number: 20 <= number <= 50, numbers))

def student_scores_to_grades(student_scores:dict) -> dict:
    students_grades = {}
    for key, value in student_scores.items():
        students_grades[key] = get_grade(value)
    return students_grades


def get_grade(grade:int) -> str:
    if 90 < grade < 100:
        return "Outstanding"
    elif grade > 80:
        return "Exceeds Expectations"
    elif grade > 70:
        return "Acceptable"
    elif grade > 0:
        return "Fail"
    else:
        return "Invalid score, only 0 - 100 supported"