from unittest import TestCase
from sum_of_even_number import sum_of_even_number

class TestSumOfEvenNumber(TestCase):
    def test_that_sum_of_even_number_exist(self):
        sum_of_even_number([1,2,3,4])
        
    def test_that_sum_of_even_number_return_correct_value(self):
        actual = sum_of_even_number([1, 5, 7, 3, 2, 9, 8,10])
        expected = 3
        self.assertEqual(actual, expected)
