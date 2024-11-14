from unittest import TestCase
from tddcornflakes import divide_or_square, future_investment_amount, only_floats, my_discount

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
        
    def test_that_future_investment_amount_returns_correct_value_when_positive_integer_or_float_is_entered(self):
        actual = future_investment_amount(100_000, 0.05, 3)
        expected = 579_181.61
        self.assertEqual(actual, expected)
        actual = future_investment_amount(30_000, 0.02, 3)
        expected = 61_196.62
        self.assertEqual(actual, expected)
        
    def test_that_future_investment_amount_raise_exception_for_negative_value(self):
        self.assertRaises(ValueError, future_investment_amount, -10000, 0.3, 3)
        self.assertRaises(ValueError, future_investment_amount, 10000, -0.3, 3)
        self.assertRaises(ValueError, future_investment_amount, 10000, 0.3, -3)
        
    def test_that_future_investment_amount_raise_exception_for_string_value(self):
        self.assertRaises(TypeError, future_investment_amount, "p", "r", "t")
        self.assertRaises(TypeError, future_investment_amount, 100_020, 0.65, "9")
        self.assertRaises(TypeError, future_investment_amount, 100_020, "0.65", 9)
        self.assertRaises(TypeError, future_investment_amount, "100_020", 0.65, 9)
    
    def test_that_future_investment_amount_return_correct_value_when_no_argument_is_entered(self):
        actual = future_investment_amount()
        expected = 0
        self.assertEqual(actual, expected)
    
    def test_that_future_investment_amount_return_correct_value_when_only_one_argument_is_entered(self):
        actual = future_investment_amount(investment_amount = 100_000)
        expected = 100_000
        self.assertEqual(actual, expected)
        actual = future_investment_amount(monthly_interest_rate = 0.5)
        expected = 0
        self.assertEqual(actual, expected)
        actual = future_investment_amount(year = 5)
        expected = 0
        self.assertEqual(actual, expected)
        
    def test_that_future_investment_amount_return_correct_value_when_only_two_argument_is_entered(self):
        actual = future_investment_amount(investment_amount = 100_000, monthly_interest_rate = 0.5)
        expected = 100_000
        self.assertEqual(actual, expected)
        actual = future_investment_amount(investment_amount = 100_000, year = 5)
        expected = 100_000
        self.assertEqual(actual, expected)
        actual = future_investment_amount(monthly_interest_rate = 0.5, year = 5)
        expected = 0
        self.assertEqual(actual, expected)
        
        
class TestOnlyFloatsFunction(TestCase):
    def test_that_only_floats_exist(self):
        only_floats(23, 7)
    def test_that_only_floats_returns_0_when_no_argument_is_float(self):
        actual = only_floats(23,7)
        expected = 0
        self.assertEqual(actual, expected)
        actual = only_floats(1, 2)
        expected = 0
        self.assertEqual(actual, expected)
    def test_that_only_floats_returns_1_when_only_one_argument_is_float(self):
        actual = only_floats(23, 4.5)
        expected = 1
        self.assertEqual(actual, expected)
        actual = only_floats(23.4, 44)
        expected = 1
        self.assertEqual(actual, expected)
    
    def test_that_only_floats_returns_2_if_both_argument_are_float(self):
        actual = only_floats(23.4, 4.5)
        expected = 2
        self.assertEqual(actual, expected)
        actual = only_floats(23.43, 55.44)
        expected = 2
        self.assertEqual(actual, expected)
    
    def test_that_only_floats_returns_correct_value_when_one_or_two_negative_argument_is_entered(self):
        actual = only_floats(-23.43, 4.5)
        expected = 2
        self.assertEqual(actual, expected)
        actual = only_floats(23.43, -55.44)
        expected = 2
        self.assertEqual(actual, expected)
        actual = only_floats(-23.43, -55.44)
        expected = 2
        self.assertEqual(actual, expected)
        actual = only_floats(23, -55.44)
        expected = 1
        self.assertEqual(actual, expected)
        actual = only_floats(23, -55)
        expected = 0
        self.assertEqual(actual, expected)
        
    def test_that_only_floats_raise_exception_when_only_argument_is_entered(self):
        self.assertRaises(TypeError, only_floats, "23.5")

    def test_that_only_floats_raise_exception_when_no_argument_is_entered(self):
        self.assertRaises(TypeError, only_floats)
        
    def test_that_only_floats_raise_exception_when_a_string_argument_is_entered(self):
        self.assertRaises(TypeError, only_floats, "90", "89.7")
        
class TestMyDiscount(TestCase):
    def test_that_my_discount_exist(self):
        my_discount(150, 15)
    def test_that_my_discount_returns_correct_value_with_two_positive_integer_arguments(self):
        actual = my_discount(150, 15)
        expected = 127.5
        self.assertEqual(actual, expected)
        
    def test_that_my_discount_returns_correct_value_with_two_positive_float_arguments(self):
        actual = my_discount(150.3, 15.2)
        expected = 127.45
        self.assertEqual(actual, expected)
        
    def test_that_my_discount_raises_exception_with_one_or_more_negative_integer_argument(self):
        self.assertRaises(ValueError, my_discount, -2_300, 10)
        self.assertRaises(ValueError, my_discount, 2_300, -10)
        self.assertRaises(ValueError, my_discount, -2_300, -10)
    def test_that_my_discount_raises_exception_with_one_or_more_negative_float_argument(self):
        self.assertRaises(ValueError, my_discount, -2_300.45, 10.25)
        self.assertRaises(ValueError, my_discount, 2_300.45, -10.25)
        self.assertRaises(ValueError, my_discount, -2_300.45, -10.25)
    def test_that_my_discount_raises_exception_with_one_or_more_string_argument(self):
        self.assertRaises(TypeError, my_discount, "-2_300", 10)
        self.assertRaises(TypeError, my_discount, 2_300, "-10")
        self.assertRaises(TypeError, my_discount, "-2_300", "-10")
    def test_that_my_discount_raises_exception_with_zero_or_one_argument(self):
        self.assertRaises(TypeError, my_discount, price = 2_300)
        self.assertRaises(TypeError, my_discount, discount = 10)

