from unittest import TestCase
from sum_of_even import sum_of_even

class TestSumOfEven(TestCase):
    def test_that_sum_of_even_exist(self):
        sum_of_even([2,7,9,17,19,2,8,10])
    
    def test_that_sum_of_even_return_correct_value(self):
        actual = sum_of_even([2,7,9,17,19,2,8,10])
        expected = 22
        self.assertEqual(actual, expected)
