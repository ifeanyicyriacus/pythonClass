from unittest import TestCase
from tddcornflakes import divide_or_square, future_investment_amount

class TestDivideOrSquareFunction(TestCase):
    def test_that_divide_or_square_exist(self):
        divide_or_square(5)
        
    def test_that_divide_or_square_returns_the_square_root_of_positive_integer_argument_if_it_is_divisible_by_5(self):
        actual = divide_or_square(25)
        expected = 5
        self.assertEqual(actual, expected)
        actual = divide_or_square(20)
        expected = 4.472
        self.assertEqual(actual, expected)
        
    def test_that_divide_or_square_returns_the_remainder_of_positive_integer_argument_divided_by_5_if_it_not_divisible_by_5(self):
        actual = divide_or_square(24)
        expected = 4
        self.assertEqual(actual, expected)
        actual = divide_or_square(32)
        expected = 2
        self.assertEqual(actual, expected)
        
    def test_that_divide_or_square_returns_the_remainder_of_all_positive_float_argument_divided_by_5(self):
        actual = divide_or_square(24.3)
        expected = 4.3
        self.assertEqual(actual, expected)
        actual = divide_or_square(32.23)
        expected = 2.23
        self.assertEqual(actual, expected)
        actual = divide_or_square(25.5)
        expected = 0.5
        self.assertEqual(actual, expected)
        actual = divide_or_square(20.15)
        expected = 0.15
        self.assertEqual(actual, expected)
    
    def test_that_divide_or_square_returns_the_remainder_of_all_negative_float_argument_divided_by_5(self):
        actual = divide_or_square(-24.3)
        expected = 0.7
        self.assertEqual(actual, expected)
        actual = divide_or_square(-32.23)
        expected = 2.77
        self.assertEqual(actual, expected)
        actual = divide_or_square(-25.5)
        expected = 4.5
        self.assertEqual(actual, expected)
        actual = divide_or_square(-20.15)
        expected = 4.85
        self.assertEqual(actual, expected)
        
    def test_that_divide_or_square_raise_exception_for_negative_integer_argument_divisible_by_5(self):
        self.assertRaises(ValueError, divide_or_square, -25)
        self.assertRaises(ValueError, divide_or_square, -45)
        
    def test_that_divide_or_square_returns_the_remainder_of_negative_integer_argument_divided_by_5_if_not_divisible_by_5(self):
        actual = divide_or_square(-24)
        expected = 1
        self.assertEqual(actual, expected)
        actual = divide_or_square(-32)
        expected = 3
        self.assertEqual(actual, expected)
        actual = divide_or_square(-82)
        expected = 3
        self.assertEqual(actual, expected)
        
class TestFutureInvestmentAmountFunction(TestCase):
    def test_that_future_investment_amount_exist(self):
        future_investment_amount(1, 2, 3)
    
    #def test_that_future_investment_amount_does_not_raise_exception_if_any_argument_is_missing(self):
        #self.assertRaises(TypeError, future_investment_amount)
    
    def test_that_future_investment_amount_returns_correct_value_when_positive_integer_or_float_is_entered(self):
        actual = future_investment_amount(100_000, 0.05, 3)
        expected = 579_181.61
        self.assertEqual(actual, expected)
        actual = future_investment_amount(30_000, 0.02, 3)
        expected = 61_196.62
        self.assertEqual(actual, expected)
    
    
    
class TestOnlyFloatsFunction(TestCase):
    ...
    
class TestMyDiscount(TestCase):
    ...

