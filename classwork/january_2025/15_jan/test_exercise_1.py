from unittest import TestCase
from exercise_1 import *

class TestOddEvenFunction(TestCase):
	def test_odd_even_count_return_correct_value(self):
	    input_list_1 = [1, 2, 3, 6, 8, 10, 1]
	    input_list_2 = [5, 3, 7, 9, 2, 8]
	    actual = odd_even_count(input_list_1)
	    expected = [3, 4]
	    self.assertEqual(actual, expected)
	    actual = odd_even_count(input_list_2)
	    expected = [4, 2]
	    self.assertEqual(actual, expected)
	    

