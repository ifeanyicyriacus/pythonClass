from unittest import TestCase
from primenumber import get_prime_numbers, is_prime

class TestGetPrimeNumbersFunction(TestCase):
    def test_that_get_prime_numbers_exist(self):
        get_prime_numbers(20)
        
    def test_that_get_print_number_return_correct_value(self):
        actual = get_prime_numbers(20)
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        self.assertEqual(actual, expected)
        actual = get_prime_numbers(8)
        expected = [2, 3, 5, 7]
        self.assertEqual(actual, expected)
        
class TestIsPrimeFunction(TestCase):
    def test_that_is_prime_exist(self):
        is_prime(20)
        
    def test_that_get_print_number_return_correct_value(self):
        actual = is_prime(20)
        expected = False
        self.assertEqual(actual, expected)
        actual = is_prime(19)
        expected = True
        self.assertEqual(actual, expected)

