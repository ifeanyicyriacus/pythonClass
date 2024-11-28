from unittest import TestCase
from boolean_for_even_or_odd import boolean_for_even_or_odd

class TestSumOfEvenNumber(TestCase):
    def test_that_boolean_for_even_or_odd_exist(self):
        boolean_for_even_or_odd([1,2,3,4])
        
    def test_that_boolean_for_even_or_odd_return_correct_value(self):
        actual = boolean_for_even_or_odd([1, 5, 7, 3, 2, 9, 8,10])
        expected = [False, False, False, False, True, False, True, True]
        self.assertEqual(actual, expected)
