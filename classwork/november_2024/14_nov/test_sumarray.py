from unittest import TestCase
from sumarray import get_summation

class TestArraySummation(TestCase):
    def test_that_get_summation_exist(self):
        get_summation([1, 2, 3, 4, 5])
        
    def test_that_get_summation_return_correct_value_for_integer_value(self):
        actual = get_summation([1, 2, 3, 4, 5])
        expected = 15
        self.assertEqual(actual, expected)
        actual = get_summation([1, 2, 3, 4, 5, 6])
        expected = 21
        self.assertEqual(actual, expected)
        
    def test_that_get_summation_return_correct_value_for_float_value(self):
        actual = get_summation([1.2, 2.5, 3.54, 4.2, 5.4])
        expected = 16.84
        self.assertEqual(actual, expected)
        
    def test_that_get_summation_returns_correct_value_for_negative_value(self):
        actual = get_summation([-1.2, -2.5, -3.54, -4.2, -5.4])
        expected = -16.84
        self.assertEqual(actual, expected)
        actual = get_summation([-1, -2, -3, -4, -5, -6])
        expected = -21
        self.assertEqual(actual, expected)
        
    def test_that_get_summation_returns_zero_if_ther_are_no_argument(self):
        actual = get_summation([])
        expected = 0
        self.assertEqual(actual, expected)
    
    def test_that_summation_throws_exception_for_non_list_value(self):
        self.assertRaises(TypeError, get_summation, 12, 21, 34)
        
