from unittest import TestCase
from purewater import *

class TestFindIndexFunction(TestCase):
    def test_that_find_index_function_exit(self):
        find_index([""], "")
    
    def test_that_find_index_function_returns_expected_result(self):
        expected = find_index([12, 17, 24, 32, 14], 24)
        actual = "index 2"
        self.assertEqual(expected, actual)
    
    def test_that_find_index_function_returns_expected_result_when_keyword_not_found(self):
        expected = find_index([12, 17, 24, 32, 14], 54)
        actual = "not available"
        self.assertEqual(expected, actual)
        
class TestPositiveNegativeAndZerosCountFunction(TestCase):
    def test_that_positive_negative_and_zeros_count_function_exist(self):
        positive_negative_and_zeros_count([])
        
    def test_that_positive_negative_and_zeros_count_function_returns_correct_value(self):
        expected = positive_negative_and_zeros_count([15, 34, -1, 24, -7, 9, 0])
        zeros = 1
        positives = 4
        negatives = 2
        actual = f"positives: {positives}\nnegatives: {negatives}\nzeros: {zeros}"
        self.assertEqual(expected, actual)
