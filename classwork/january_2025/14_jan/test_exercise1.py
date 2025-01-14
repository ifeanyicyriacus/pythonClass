from unittest import TestCase
from exercise1 import *

class TestParseEvenDigitFunction(TestCase):
    def test_that_parse_even_digit_exist(self):
        self.assertEqual(parse_even_digit(""), [])

    def test_that_parse_even_digit_returns_correct_value(self):
        actual = parse_even_digit("73HAdSdF39dm")
        expected = []
        self.assertEqual(actual, expected)

class TestNumberSquareFunction(TestCase):
    def test_that_number_to_square_dict_return_correct_value(self):
        self.assertEqual(number_to_square_dict(9), {1:9, 2:81})

# if __name__ == '__main__':
#     unittest.main()
