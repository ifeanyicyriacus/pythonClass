from unittest import TestCase
from morningtea import number_square, get_numbers_greater_than_10, words_palindrome_checker, pluck_numbers_from

class TestNumberSquareFunction(TestCase):
	def test_that_number_square_exist(self):
		number_square(4)
		
	def test_that_number_square_return_correct_value(self):
		actual = number_square(4)
		expected = [1, 4, 9, 16]
		self.assertEqual(actual, expected)
		
class TestNumbersGreaterThan10Function(TestCase):
	def test_that_get_numbers_greater_than_10_exist(self):
		get_numbers_greater_than_10([1, 5, 12, 15, 8])
    		
	def test_that_get_numbers_greater_than_10_return_correct_value(self):
		actual = get_numbers_greater_than_10([1, 5, 12, 15, 8])
		expected = [12, 15]
		self.assertEqual(actual, expected)
		
class TestWordsPalindromeCheckerFunction(TestCase):
	def test_that_words_palindrome_checker_exist(self):
		words_palindrome_checker(['madam', 'apple', 'racecar'])
    		
	def test_that_words_palindrome_checker_return_correct_value(self):
		actual = words_palindrome_checker(['madam', 'apple', 'racecar'])
		expected = [True, False, True]
		self.assertEqual(actual, expected)
		
class TestPluckNumbersFromFunction(TestCase):
	def test_that_pluck_numbers_from_exist(self):
		pluck_numbers_from('abc123def456')
    		
	def test_that_words_palindrome_checker_return_correct_value(self):
		actual = pluck_numbers_from('abc123def456')
		expected = [1, 2, 3, 4, 5, 6]
		self.assertEqual(actual, expected)
		
		actual = pluck_numbers_from('222abc123def456')
		expected = [2, 2, 2, 1, 2, 3, 4, 5, 6]
		self.assertEqual(actual, expected)
