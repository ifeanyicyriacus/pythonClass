from unittest import TestCase
from multiple_of_3_between import multiple_of_3_between

class TestMultipleOf3BetweenFunction(TestCase):
    def test_that_multiple_of_3_between_exist(self):
        multiple_of_3_between(3, 30)
        
    def test_that_multiple_of_3_between_return_correct_value(self):
        actual = multiple_of_3_between(3, 30)
        expected = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
        self.assertEqual(actual, expected)
