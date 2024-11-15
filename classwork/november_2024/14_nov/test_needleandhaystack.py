from unittest import TestCase
from needleandhaystack import remove_character

class TestRemoveCharacterFunction(TestCase):
    def test_that_remove_character_exist(self):
        remove_character("apple pie", "e")
    
    def test_that_remove_character_returns_correct_value_when_both_argument_are_string(self):
        actual = remove_character("apple pie", "e")
        expected = "appl pi"
        self.assertEqual(actual, expected)
        actual = remove_character("Scooby doo", "o")
        expected = "Scby d"
        self.assertEqual(actual, expected)
        actual = remove_character("Scoooby doo", "oo")
        expected = "Scoby d"
        self.assertEqual(actual, expected)
    
    def test_that_remove_character_return_correct_value_when_its_argument_are_list_and_string(self):
        actual = remove_character(["apple", "pie","eee"], "e")
        expected = ["appl", "pi"]
        self.assertEqual(actual, expected)
        actual = remove_character(["apple", "Banana","carrot"], "a")
        expected = ["pple", "Bnn", "crrot"]
        self.assertEqual(actual, expected)
        
    def test_that_remove_character_return_list_unchanged_if_second_argument_not_found(self):
        actual = remove_character(["apple", "pie","eee"], "v")
        expected = ["apple", "pie","eee"]
        self.assertEqual(actual, expected)
        actual = remove_character(["apple", "Banana","carrot"], "m")
        expected = ["apple", "Banana","carrot"]
        self.assertEqual(actual, expected)
    
    def test_that_remove_character_return_string_unchanged_if_second_argument_not_found(self):
        actual = remove_character("apple pie", "q")
        expected = "apple pie"
        self.assertEqual(actual, expected)
        actual = remove_character("Scooby doo", "r")
        expected = "Scooby doo"
        self.assertEqual(actual, expected)
        actual = remove_character("Scoooby doo", "dd")
        expected = "Scoooby doo"
        self.assertEqual(actual, expected)
        
    def test_that_remove_character_returns_first_argument_when_its_second_argument_is_not_given(self):
        actual = remove_character("Scooby doo")
        expected = "Scooby doo"
        self.assertEqual(actual, expected)
        actual = remove_character("Scoooby doo")
        expected = "Scoooby doo"
        self.assertEqual(actual, expected)
        actual = remove_character(["apple", "pie","eee"])
        expected = ["apple", "pie","eee"]
        self.assertEqual(actual, expected)
        actual = remove_character(["apple", "Banana","carrot"])
        expected = ["apple", "Banana","carrot"]
        self.assertEqual(actual, expected)
        
