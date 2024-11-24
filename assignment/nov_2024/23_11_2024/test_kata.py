from unittest import TestCase
from kata import *

class TestIsEvenFunction(TestCase):
    def test_that_is_even_exists(self):
        is_even(13)
    def test_that_is_even_returns_correct_value(self):
        actual = is_even(13)
        expected = False
        self.assertEqual(actual, expected)
        actual = is_even(14)
        expected = True
        self.assertEqual(actual, expected)


class TestIsPrimeNumberFunction(TestCase):
    def test_that_is_prime_number_exists(self):
        is_prime_number(13)
    def test_that_is_prime_number_returns_correct_value(self):
        actual = is_prime_number(13)
        expected = True
        self.assertEqual(actual, expected)
        actual = is_prime_number(24)
        expected = False
        self.assertEqual(actual, expected)

class TestSubtractFunction(TestCase):
    def test_that_subtract_exists(self):
        subtract(13, 2)
    def test_that_subtract_returns_correct_value(self):
        actual = subtract(7, 3)
        expected = 4
        self.assertEqual(actual, expected)
        actual = subtract(3, 7)
        expected = 4
        self.assertEqual(actual, expected)
        
class TestDivideFunction(TestCase):
    def test_that_divide_exists(self):
        divide(13, 2)
    def test_that_subtract_returns_correct_value(self):
        actual = divide(5, 0)
        expected = 0.0
        self.assertEqual(actual, expected)
        actual = divide(5, 2)
        expected = 2.5
        self.assertEqual(actual, expected)
        
class TestFactorOfFunction(TestCase):
    def test_that_factor_of_exists(self):
        factor_of(10)
    def test_that_factor_of_returns_correct_value(self):
        actual = factor_of(10)
        expected = 4
        self.assertEqual(actual, expected)
        actual = factor_of(15)
        expected = 4
        self.assertEqual(actual, expected)
        
class TestIsSquareFunction(TestCase):
    def test_that_is_square_exists(self):
        is_square(10)
    def test_that_is_square_returns_correct_value(self):
        actual = is_square(25)
        expected = True
        self.assertEqual(actual, expected)
        actual = is_square(10)
        expected = False
        self.assertEqual(actual, expected)
        
class TestIsPalindromeFunction(TestCase):
    def test_that_is_palindrome_exists(self):
        is_palindrome(10)
    def test_that_is_palindrome_returns_correct_value(self):
        actual = is_palindrome(5225)
        expected = True
        self.assertEqual(actual, expected)
        actual = is_palindrome(54345)
        expected = True
        self.assertEqual(actual, expected)
        actual = is_palindrome(53345)
        expected = False
        self.assertEqual(actual, expected)
        
class TestFactorialOfFunction(TestCase):
    def test_that_factorial_of_exists(self):
        factorial_of(10)
    def test_that_factorial_of_returns_correct_value(self):
        actual = factorial_of(5)
        expected = 120
        self.assertEqual(actual, expected)
        actual = factorial_of(10)
        expected = 3628800
        self.assertEqual(actual, expected)
        
class TestSquareOfFunction(TestCase):
    def test_that_square_of_exists(self):
        square_of(10)
    def test_that_square_of_returns_correct_value(self):
        actual = square_of(10)
        expected = 100
        self.assertEqual(actual, expected)
        actual = square_of(5)
        expected = 25
        self.assertEqual(actual, expected)
