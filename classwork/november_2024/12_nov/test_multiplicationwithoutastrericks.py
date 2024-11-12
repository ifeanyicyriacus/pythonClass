from unittest import TestCase
import multiplicationwithoutastrericks

class TestMultiplicationWithoutAstrericksFunction(TestCase):
    def test_that_get_product_exists(self):
        multiplicationwithoutastrericks.get_product(2, 3)
    
    def test_that_get_product_returns_correct_value_with_positive_integers(self):
        actual = multiplicationwithoutastrericks.get_product(2, 3)
        expected = 6
        self.assertEqual(actual, expected)
        actual = multiplicationwithoutastrericks.get_product(5, 2)
        expected = 10
        self.assertEqual(actual, expected)
        
    def test_that_get_product_returns_correct_value_with_positive_float_arguments(self):
        actual = multiplicationwithoutastrericks.get_product(2, 3.1)
        expected = 6.2
        self.assertEqual(actual, expected)
        actual = multiplicationwithoutastrericks.get_product(5.2, 2)
        expected = 10.4
        self.assertEqual(actual, expected)
        actual = multiplicationwithoutastrericks.get_product(5.2, 2.2)
        expected = 11.44
        self.assertEqual(actual, expected)
        actual = multiplicationwithoutastrericks.get_product(100, 0.002)
        expected = 0.2
        self.assertEqual(actual, expected)
    
    def test_that_get_product_returns_correct_value_with_negative_integer_arguments(self):
        actual = multiplicationwithoutastrericks.get_product(-2, 3)
        expected = -6
        self.assertEqual(actual, expected)
        actual = multiplicationwithoutastrericks.get_product(5, -2)
        expected = -10
        self.assertEqual(actual, expected)
        actual = multiplicationwithoutastrericks.get_product(-6, -3)
        expected = 18
        self.assertEqual(actual, expected)
    
    def test_that_get_product_returns_correct_value_with_negative_float_arguments(self):
        actual = multiplicationwithoutastrericks.get_product(2.1, -3.1)
        expected = -6.51
        self.assertEqual(actual, expected)
        actual = multiplicationwithoutastrericks.get_product(-5.2, 2.3)
        expected = -11.96
        self.assertEqual(actual, expected)
        actual = multiplicationwithoutastrericks.get_product(-5.2, -2.2)
        expected = 11.44
        self.assertEqual(actual, expected)
    
    def test_that_get_product_handles_only_one_argument(self):
        actual = multiplicationwithoutastrericks.get_product(2.1)
        expected = 2.1
        self.assertEqual(actual, expected)
        actual = multiplicationwithoutastrericks.get_product(-3.1)
        expected = -3.1
        self.assertEqual(actual, expected)
    
    def test_that_get_product_returns_zero_if_any_or_both_of_it_argument_is_zero(self):
        actual = multiplicationwithoutastrericks.get_product(0, -3.1)
        expected = 0
        self.assertEqual(actual, expected)
        actual = multiplicationwithoutastrericks.get_product(-5.2, 0)
        expected = 0
        self.assertEqual(actual, expected)
        actual = multiplicationwithoutastrericks.get_product(0, 0)
        expected = 0
        self.assertEqual(actual, expected)
        actual = multiplicationwithoutastrericks.get_product(0)
        expected = 0
        self.assertEqual(actual, expected)
        
    def test_that_get_product_raise_exception_with_invalid_input(self):
        self.assertRaises(TypeError, multiplicationwithoutastrericks.get_product, 2,"hi")
        self.assertRaises(TypeError, multiplicationwithoutastrericks.get_product, "hi", 2)
        self.assertRaises(TypeError, multiplicationwithoutastrericks.get_product, "hi","hi")
        
