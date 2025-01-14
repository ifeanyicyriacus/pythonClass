# Recap of List, Dictionary, list comprehension and testing

import math

def parse_even_digit(text:str) -> list:
    return [x for x in list([int(x) for x in text if x.isdigit()]) if x % 2 == 0]

def number_to_square_dict(number:int) -> dict:
    return {1: number, 2: math.pow(number, 2)}

def filter_between_20_and_50(numbers:list) -> list:
    return list(filter(lambda number: 20 <= number <= 50, numbers))

def student_scores_to_grades(student_scores:dict) -> dict:
    return {key: get_grade(value) for key, value in student_scores.items()}

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

def cohort_detail_zipper(list1, list2):
    return dict(zip(list1, list2))

def complex_dictionary(school_records:dict) -> list:
   return [
       school_records["class_2"]["students"][1]["name"],
       school_records["class_2"]["students"][1]["scores"]
   ]

def calculate_average_math_score (student_scores:dict) -> float:
    total = 0
    number_of_students = 0
    for classes in student_scores.values():
        for students in classes["students"]:
            total += students["scores"]["Math"]
            number_of_students += 1
    return total / number_of_students
