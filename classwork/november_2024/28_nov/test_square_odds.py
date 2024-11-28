from unittest import TestCase
from square_odds import square_odds

class TestMultipleOf3BetweenFunction(TestCase):
    def test_that_multiple_of_3_between_exist(self):
        square_odds([3, 30])
        
    def test_that_multiple_of_3_between_return_correct_value(self):
        actual = square_odds([10, 3, 7, 1, 9, 4, 2, 8, 5, 6])
        expected = [9, 49, 1, 81, 25]
        self.assertEqual(actual, expected)
