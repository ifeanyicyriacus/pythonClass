from unittest import TestCase
from mondaymorningfunctions import *

class TestGetSwitchedListFunction(TestCase):
    def test_that_get_switched_list_exists(self):
        get_switched_list([12,23,3,4,5], 3)
    
    def test_that_get_switched_list_return_correct_value(self):
        actual = get_switched_list([12,23,3,4,5], 3)
        expected = [4, 5, 12, 23, 3]
        self.assertEqual(actual, expected)
        actual = get_switched_list([12,23,3,4,5], 2)
        expected = [3, 4, 5, 12, 23]
        self.assertEqual(actual, expected)
    
class TestSplitInHalfFunction(TestCase):
    def test_that_split_in_half_exists(self):
        split_in_half([12,23,3,4,5])
    
    def test_that_split_in_half_return_correct_value(self):
        actual = split_in_half([12, 23, 3, 4, 5])
        expected = [[12, 23, 3], [4, 5]]
        self.assertEqual(actual, expected)
        actual = split_in_half([12, 23, 8, 3, 4, 5])
        expected = [[12, 23, 8], [3, 4, 5]]
        self.assertEqual(actual, expected)    

class TestCheckIfListAreEvenFunction(TestCase):
    def test_that_check_if_list_are_even_exists(self):
        check_if_list_are_even([12,23,3,4,5])
    
    def test_that_check_if_list_are_even_return_correct_value(self):
        actual = check_if_list_are_even([12, 23, 3, 4, 5])
        expected = [True, False, False, True, False]
        self.assertEqual(actual, expected)
        actual = check_if_list_are_even([1, 24, 12, 23, 13, 100, 4, 5])
        expected = [False, True, True, False, False, True, True, False]
        self.assertEqual(actual, expected)
