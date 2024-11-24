from unittest import TestCase
from listfunction import *

list_1 = [19, 32, 133, 40, 56, 40, 70]
list_2 = [60, 82, 9, 36, 90]
number_1 = 76328656
number_2 = 102003000
text_1 = "madAm"
text_2 = "Apple"

class TestFindLargestFromFunction(TestCase):
  def test_that_find_largest_from_exist(self):
    find_largest_from(list_1)

  def test_that_find_largest_from_return_correct_value(self):
    actual = find_largest_from(list_1)
    expected = 133
    self.assertEqual(actual, expected)


class TestReverseListFunction(TestCase):
  def test_that_reverse_list_exist(self):
    reverse_list(list_1)

  def test_that_reverse_list_return_correct_value(self):
    actual = reverse_list(list_1)
    expected = [70, 40, 56, 40, 133, 32, 19]
    self.assertEqual(actual, expected)

class TestCheckIfExistFunction(TestCase):
  def test_that_check_if_exist_exists(self):
    check_if_exist(list_1, 20)

  def test_that_check_if_return_correct_value(self):
    actual = check_if_exist(list_1, 20)
    expected = False
    self.assertEqual(actual, expected)
    actual = check_if_exist(list_1, 19)
    expected = True
    self.assertEqual(actual, expected)

class TestReturnOddPositionElementFunction(TestCase):
  def test_that_return_odd_position_element_exists(self):
    return_odd_position_element(list_1)

  def test_that_return_odd_position_element_return_correct_value(self):
    actual = return_odd_position_element(list_1)
    expected = [19, 133, 56, 70]
    self.assertEqual(actual, expected)
    actual = return_odd_position_element(list_2)
    expected = [60, 9, 90]
    self.assertEqual(actual, expected)
    
class TestReturnEvenPositionElementFunction(TestCase):
  def test_that_return_even_position_element_exists(self):
    return_even_position_element(list_1)

  def test_that_return_even_position_element_return_correct_value(self):
    actual = return_even_position_element(list_1)
    expected = [32, 40, 40]
    self.assertEqual(actual, expected)
    actual = return_even_position_element(list_2)
    expected = [82,36]
    self.assertEqual(actual, expected)    
    
class TestGetRunningTotalFunction(TestCase):
  def test_that_get_running_total_exists(self):
    get_running_total(list_1)

  def test_that_get_running_total_return_correct_value(self):
    actual = get_running_total(list_1)
    expected = 390
    self.assertEqual(actual, expected)
    actual = get_running_total(list_2)
    expected = 277
    self.assertEqual(actual, expected)
    
class TestCheckIfPalindromeFunction(TestCase):
  def test_that_check_if_palindrome_exists(self):
    check_if_palindrome(text_1)

  def test_that_check_if_palindrome_return_correct_value(self):
    actual = check_if_palindrome(text_1)
    expected = True
    self.assertEqual(actual, expected)
    actual = check_if_palindrome(text_2)
    expected = False
    self.assertEqual(actual, expected) 
    
class TestSumUsingForLoopFunction(TestCase):
  def test_that_sum_using_for_loop_exists(self):
    sum_using_for_loop(list_1)

  def test_that_sum_using_for_loop_return_correct_value(self):
    actual = sum_using_for_loop(list_1)
    expected = 390
    self.assertEqual(actual, expected)
    actual = sum_using_for_loop(list_2)
    expected = 277
    self.assertEqual(actual, expected) 
    
class TestSumUsingWhileLoopFunction(TestCase):
  def test_that_sum_using_while_loop_exists(self):
    sum_using_while_loop(list_1)

  def test_that_sum_using_while_loop_return_correct_value(self):
    actual = sum_using_while_loop(list_1)
    expected = 390
    self.assertEqual(actual, expected)
    actual = sum_using_while_loop(list_2)
    expected = 277
    self.assertEqual(actual, expected) 
    
class TestConcatinateListsFunction(TestCase):
  def test_that_concatinate_lists_exists(self):
    concatinate_lists(list_1, list_2)

  def test_that_concatinate_lists_return_correct_value(self):
    actual = concatinate_lists(list_1, list_2)
    expected = [19, 32, 133, 40, 56, 40, 70, 60, 82, 9, 36, 90]
    self.assertEqual(actual, expected)
    actual = concatinate_lists(list_2, list_1)
    expected = [60, 82, 9, 36, 90, 19, 32, 133, 40, 56, 40, 70]
    self.assertEqual(actual, expected) 
    
class TestAlternatingConcatinationFunction(TestCase):
  def test_that_alternating_concatination_exists(self):
    alternating_concatination(list_1, list_2)

  def test_that_alternating_concatination_return_correct_value(self):
    actual = alternating_concatination(list_1, list_2)
    expected = [19, 60, 32, 82, 133, 9, 40, 36, 56, 90, 40, 70]
    self.assertEqual(actual, expected)
    actual = alternating_concatination(list_2, list_1)
    expected = [60, 19, 82, 32, 9, 133, 36, 40, 90, 56, 40, 70]
    self.assertEqual(actual, expected) 
    
class TestNumberToListOfDigitFunction(TestCase):
  def test_that_number_to_list_of_digit_exists(self):
    number_to_list_of_digit(number_1)

  def test_that_number_to_list_of_digit_return_correct_value(self):
    actual = number_to_list_of_digit(number_1)
    expected = [7, 6, 3, 2, 8, 6, 5, 6]
    self.assertEqual(actual, expected)
    actual = number_to_list_of_digit(number_2)
    expected = [1, 0, 2, 0, 0, 3, 0, 0, 0]
    self.assertEqual(actual, expected)
