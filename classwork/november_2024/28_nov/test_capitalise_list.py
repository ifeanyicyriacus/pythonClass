from unittest import TestCase
from capitalise_list import capitalise_list

class TestCapitaliseListFunction(TestCase):
    def test_that_capitalise_list_exist(self):
        capitalise_list(["red", "orange", "yellow", "green", "blue"])
        
    def test_that_capitalise_list_return_correct_value(self):
        actual = capitalise_list(["red", "orange", "yellow", "green", "blue"])
        expected = ["Red", "Orange", "Yellow", "Green", "Blue"]
        self.assertEqual(actual, expected)
