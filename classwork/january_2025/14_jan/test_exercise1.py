from unittest import TestCase
from exercise1 import *

class TestParseEvenDigitFunction(TestCase):
    def test_that_parse_even_digit_exist(self):
        self.assertEqual(parse_even_digit(""), [])

    def test_that_parse_even_digit_returns_correct_value(self):
        actual = parse_even_digit("73H2AdS8d9F39dm")
        expected = [2, 8]
        self.assertEqual(actual, expected)

class TestNumberSquareFunction(TestCase):
    def test_that_number_to_square_dict_return_correct_value(self):
        self.assertEqual(number_to_square_dict(9), {1:9, 2:81})

class TestFilterBetween20And50Function(TestCase):
    def test_that_filter_between_20_and_50_exist(self):
        self.assertEqual(filter_between_20_and_50([]), [])

    def test_that_filter_between_50_and_20_return_correct_value(self):
        actual = filter_between_20_and_50([12, 15, 19, 21, 50, 70])
        expected = [21, 50]
        self.assertEqual(actual, expected)

class TestStudentScoresToGradesFunction(TestCase):
    def test_that_student_scores_to_grades_return_correct_value(self):
        student_scores = {'Gloria': 88,
                          'Divine': 78,
                          'Esther': 99,
                          'Mercy': 75,
                          'Uzo': 71}
        actual = student_scores_to_grades(student_scores)
        expected = {
            'Gloria': "Exceeds Expectations",
            'Divine': "Acceptable",
            'Esther': "Outstanding",
            'Mercy': "Acceptable",
            'Uzo': "Acceptable"}
        self.assertEqual(actual, expected)

class TestCohortDetailZipperFunction(TestCase):
    def test_that_cohort_detail_zipper_return_correct_value(self):
        list1 = ["cohort24", "cohort23", "cohort22"]
        list2 = ["4 months", "5 months", "6 months"]
        actual = cohort_detail_zipper(list1, list2)
        expected = {
            "cohort24" : "4 months",
            "cohort23": "5 months",
            "cohort22": "6 months"
        }
        self.assertEqual(actual, expected)

class TestComplexDictionaryFunction(TestCase):
    def test_that_complex_dictionary_return_correct_value(self):
        school_records = {
            "class_1":{
                "students": [
                    {
                        "name": "Harry",
                        "scores": {"Math": 88, "English": 76}
                     },
                    {
                        "name": "Solomon",
                        "scores": {"Math": 95, "English": 89}
                    }
                ]
            },
            "class_2":{
                "students": [
                    {
                        "name": "Daniel",
                        "scores": {"Math": 78, "English": 72}
                    },
                    {
                        "name": "Samuel",
                        "scores": {"Math": 85, "English": 80}
                    }
                ]
            }
        }
        actual = complex_dictionary(school_records)
        expected = ["Samuel", {"Math": 85, "English": 80}]
        self.assertEqual(actual, expected)

    def test_that_calculate_average_math_score_return_correct_value(self):
        school_records = {
            "class_1":{
                "students": [
                    {
                        "name": "Harry",
                        "scores": {"Math": 88, "English": 76}
                     },
                    {
                        "name": "Solomon",
                        "scores": {"Math": 95, "English": 89}
                    }
                ]
            },
            "class_2":{
                "students": [
                    {
                        "name": "Daniel",
                        "scores": {"Math": 78, "English": 72}
                    },
                    {
                        "name": "Samuel",
                        "scores": {"Math": 85, "English": 80}
                    }
                ]
            }
        }
        actual = calculate_average_math_score(school_records)
        expected = 86.5
        self.assertEqual(actual, expected)