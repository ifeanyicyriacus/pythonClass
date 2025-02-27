import unittest
from src.cornflakes.task1 import character_frequency_calculator as cfc
from src.cornflakes.task2 import swap_and_join
from src.cornflakes.task3 import add_character_to_middle_or_end as add_char
from src.cornflakes.task4 import sort_text_by_case
from src.cornflakes.task5 import find_letter_frequency


class Task1Test(unittest.TestCase):
    def test_task1_character_frequency_calculator_function(self):
        sample:str = "semicolon.africa"
        actual:dict = cfc(sample)
        expected:dict = {
            's':1, 'e':1, 'm':1, 'i':2, 'c': 2, 'o':2, 'l':1, 'n': 1, '.':1, 'a':2, 'f':1, 'r':1
        }
        self.assertEqual(actual,expected)

        sample_2:str = "ifeanyi"
        actual:dict = cfc(sample_2)
        expected:dict = {'i':2, 'f':1, 'e':1, 'a':1, 'n':1, 'y':1}
        self.assertEqual(actual,expected)


class Task2Test(unittest.TestCase):
    def test_task2_swap_and_join_function(self):
        sample1:tuple = 'abc', 'xyc'
        actual:str = swap_and_join(sample1)
        expected:str = 'xyc abc'
        self.assertEqual(actual,expected)

        sample2: tuple = 'hello', 'goodbye', 'see', 'you', 'later'
        actual: str = swap_and_join(sample2)
        expected: str = 'later you see goodbye hello'
        self.assertEqual(actual, expected)

class Task3Test(unittest.TestCase):
    def test_task3_add_character_to_middle_or_end_function(self):
        sample1:str = 'helloo'
        char:str = 'ce'
        actual:str = add_char(sample1, char)
        expected:str = 'helceloo'
        self.assertEqual(actual,expected)

        sample2:str = 'joy'
        actual:str = add_char(sample2, char)
        expected:str = 'joyce'
        self.assertEqual(actual,expected)

        sample3:str = 'laptop'
        char:str = 'lol'
        actual:str = add_char(sample3, char)
        expected:str = 'laploltop'
        self.assertEqual(actual,expected)

class Task4Test(unittest.TestCase):
    def test_task4_sort_text_by_case_function(self):
        sample1:str = "sEmIColOn"
        actual:str = sort_text_by_case(sample1)
        expected:str = 'EICOsmoln'
        self.assertEqual(actual,expected)

        sample2:str = "aFrIcA"
        actual:str = sort_text_by_case(sample2)
        expected:str = 'FIAarc'


class Task5Test(unittest.TestCase):
    def test_task5_find_letter_frequency_function(self):
        word:str = "semicolon"
        keyword:str = "o"
        actual:tuple = find_letter_frequency(word, keyword)
        expected:tuple = ('o', 2)
        self.assertEqual(actual,expected)

        word:str = "lol"
        keyword:str = "o"
        actual:tuple = find_letter_frequency(word, keyword)
        expected:tuple = ('o', 1)
        self.assertEqual(actual,expected)

