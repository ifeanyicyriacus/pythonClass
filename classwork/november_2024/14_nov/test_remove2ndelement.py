from unittest import TestCase
from remove2ndelement import remove2nd

class TestRemove2ndElementFunction(TestCase):
    def test_that_remove2ndelement_exist(self):
        remove2nd([1,2])
    
    def test_that_remove2nd_return_correct_value_with_an_integer_list_argument(self):
        actual = remove2nd([1, 2, 3, 4, 5])
        expected = [1, 3, 4, 5]
        self.assertEqual(actual, expected)
        
    def test_that_remove2nd_return_correct_value_with_a_float_list_argument(self):
        actual = remove2nd([12.2,34,56,776,89])
        expected = [12.2,56,776,89]
        self.assertEqual(actual, expected)
        
    def test_that_remove2nd_returns_correct_value_with_a_string_list_argument(self):
        actual = remove2nd(["hello", "dear", "howdy!"])
        expected = ["hello", "howdy!"]
        self.assertEqual(actual, expected)
    
    def test_that_remove2nd_returns_the_same_list_if_list_as_only_one_element(self):
        actual = remove2nd(["hello"])
        expected = 0
        self.assertEqual(actual, expected)
