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

# if __name__ == '__main__':
#     unittest.main()
