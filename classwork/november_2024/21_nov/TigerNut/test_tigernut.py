from unittest import TestCase
from tigernut import even_adder, vowel_counter, anagram_checker, prime_checker, string_palindrome_checker, reverse_string, get_average, capitalise_list, duplicate_checker, white_space_remover, get_list_intercept, sum_of_product, ignore_index, merge_and_sort, ignore_index_method_2, sort_word_list_by_length, number_factorial, sum_of_number_digit, sum_of_number_odd_digit, acronym

class TestEvenAdderFunction(TestCase):
    def test_that_even_adder_exist(self):
        even_adder([1, 2])
    
    def test_that_even_adder_return_correct_value(self):
        actual = even_adder([1, 2, 3, 4])
        expected = 6
        self.assertEqual(actual, expected)

class TestVowelCounterFunction(TestCase):
    def test_that_vowel_counter_exist(self):
        vowel_counter("Hello")
    
    def test_that_vowel_counter_return_correct_value(self):
        actual = vowel_counter("Hello")
        expected = 2
        self.assertEqual(actual, expected)
        actual = vowel_counter("Hi, how was your night. Ok.")
        expected = 7
        self.assertEqual(actual, expected)
           
class TestAnagramCheckerFunction(TestCase):
    def test_that_anagram_checker_exist(self):
        anagram_checker("hi", "iH")
    
    def test_that_anagram_checker_returns_correct_value(self):
        actual = anagram_checker("listen", "silent" )
        expected = True
        self.assertEqual(actual, expected)
        
        actual = anagram_checker("hi", "iHH")
        expected = False
        self.assertEqual(actual, expected)
        
        actual = anagram_checker("hiaa", "iaHH")
        expected = False
        self.assertEqual(actual, expected)
        
        actual = anagram_checker("live", "evil")
        expected = True
        self.assertEqual(actual, expected)
        
class TestPrimeCheckerFunction(TestCase):
    def test_that_prime_checker_exist(self):
        prime_checker(77)
        
    def test_that_prime_checker_return_correct_value(self):
        actual = prime_checker(77)
        expected = False
        self.assertEqual(actual, expected)
        
        actual = prime_checker(4)
        expected = False
        self.assertEqual(actual, expected)
        
        actual = prime_checker(1)
        expected = True
        self.assertEqual(actual, expected)
        
class TestStringPalindromeCheckerFunction(TestCase):
    def test_that_string_palindrome_checker_exist(self):
        string_palindrome_checker("madam")
    
    def test_that_string_palindrome_checker_returns_correct_value(self):
        actual = string_palindrome_checker("madam")
        expected = True
        self.assertEqual(actual, expected)
        actual = string_palindrome_checker("run")
        expected = False
        self.assertEqual(actual, expected)
        
class TestReverseStringFunction(TestCase):
    def test_that_reverse_string_exist(self):
        reverse_string("apple")
    
    def test_that_reverse_string_returns_correct_value(self):
        actual = reverse_string("apple")
        expected = "elppa"
        self.assertEqual(actual, expected)
        actual = reverse_string("aeiou")
        expected = "uoiea"
        self.assertEqual(actual, expected)
        
class TestGetAverageFunction(TestCase):
    def test_that_get_average_exist(self):
        reverse_string("apple")
    
    def test_that_get_average_returns_correct_value(self):
        actual = get_average([2.0, 3.8, 54.2])
        expected = 20.0
        self.assertEqual(actual, expected)
        actual = get_average([3, 7 ])
        expected = 5.0
        self.assertEqual(actual, expected)
        
class TestCapitaliseListFunction(TestCase):
    def test_that_capitalise_list_exist(self):
        capitalise_list(["Hi", "hello"])
    
    def test_that_capitalise_list_returns_correct_value(self):
        actual = capitalise_list(["apple", "banana", "cherry"])
        expected = ["Apple", "Banana", "Cherry"]
        self.assertEqual(actual, expected)
        actual = capitalise_list(["Hi", "hello", "howdy!", "ca va", "terve"])
        expected = ["Hi", "Hello", "Howdy!", "Ca va", "Terve"]
        self.assertEqual(actual, expected)
        
class TestDuplicateCheckerFunction(TestCase):
    def test_that_duplicate_checker_exist(self):
        duplicate_checker([12,3,44,3,33])
        
    def test_that_duplicate_checker_returns_correct_value(self):
        actual = duplicate_checker([12,3,44,3,33])
        expected = True
        self.assertEqual(actual, expected)
        actual = duplicate_checker([12,3,44,5,33])
        expected = False
        self.assertEqual(actual, expected)
        actual = duplicate_checker(["Hi", "hello", "howdy!", "ca va", "terve"])
        expected = False
        self.assertEqual(actual, expected)
    
class TestWhiteSpaceRemoverFunction(TestCase):
    def test_that_white_space_remover_exist(self):
        white_space_remover("hello world")
        
    def test_that_white_space_remover_returns_correct_value(self):
        actual = white_space_remover("hello  hi!")
        expected = "hellohi!"
        self.assertEqual(actual, expected)
        
        actual = white_space_remover("  wow    hi  !")
        expected = "wowhi!"
        self.assertEqual(actual, expected)
        
class TestGetListInterceptFunction(TestCase):
    def test_that_get_list_intercept_exist(self):
        get_list_intercept([1, 3, 5], [1, 2, 7, 3])
        
    def test_that_get_list_intercept_returns_correct_value(self):
        actual = get_list_intercept([1, 3, 5], [1, 2, 7, 3])
        expected = [1, 3]
        self.assertEqual(actual, expected)
        
        actual = get_list_intercept([3, 5, 7, 4], [1, 2, 3, 4, 5, 6])
        expected = [3, 5, 4]
        self.assertEqual(actual, expected)


class TestSumOfProductFunction(TestCase):
    def test_that_sum_of_product_exist(self):
        sum_of_product([1, 2, 3, 4])
        
    def test_that_get_list_intercept_returns_correct_value(self):
        actual = sum_of_product([1, 2, 3, 4])
        expected = 30
        self.assertEqual(actual, expected)
        actual = sum_of_product([1, 2, 3, 4, 5])
        expected = 55
        self.assertEqual(actual, expected)
        

class TestSortWordListByLengthFunction(TestCase):
    def test_that_sort_word_list_by_length_exist(self):
        sort_word_list_by_length(["apple", "cashews", "cherry"])
        
    def test_that_sort_word_list_by_length_returns_correct_value(self):
        actual = sort_word_list_by_length(["apple", "cashews", "cherry"])
        expected = ["apple", "cherry","cashews"]
        self.assertEqual(actual, expected)

class TestNumberFactorialFunction(TestCase):
    def test_that_number_factorial_exist(self):
        number_factorial(5)
        
    def test_that_number_factorial_returns_correct_value(self):
        actual = number_factorial(10)
        expected = 3_628_800
        self.assertEqual(actual, expected)
        actual = number_factorial(5)
        expected = 120
        self.assertEqual(actual, expected)
        
class TestSumOfNumberDigitFunction(TestCase):
    def test_that_sum_of_number_digit_exist(self):
        sum_of_number_digit(5)
        
    def test_that_sum_of_number_digit_returns_correct_value(self):
        actual = sum_of_number_digit(15324)
        expected = 15
        self.assertEqual(actual, expected)       
        
class TestSumOfNumberOddDigitFunction(TestCase):
    def test_that_sum_of_number_odd_digit_exist(self):
        sum_of_number_odd_digit(5)
        
    def test_that_sum_of_number_odd_digit_returns_correct_value(self):
        actual = sum_of_number_odd_digit(12345)
        expected = 9
        self.assertEqual(actual, expected)        
        
        
class TestAcronymFunction(TestCase):
    def test_that_acronym_exist(self):
        acronym("Portable Network Graphics")
        
    def test_that_acronym_returns_correct_value(self):
        actual = acronym("Portable Network Graphics")
        expected = "PNG"
        self.assertEqual(actual, expected)
        actual = acronym("portable Document format")
        expected = "PDF"
        self.assertEqual(actual, expected)


#extra task
class TestIgnoreIndexFunction(TestCase):
    def test_that_ignore_index_exist(self):
        ignore_index([1, 2, 3, 4])
        
    def test_that_ignore_index_returns_correct_value(self):
        actual = ignore_index([1, 2, 3, 4])
        expected = 30
        self.assertEqual(actual, expected)
        actual = ignore_index([1, 2, 3, 4, 5])
        expected = 60
        self.assertEqual(actual, expected)

class TestIgnoreIndexMethod2Function(TestCase):
    def test_that_ignore_index_method_2_exist(self):
        ignore_index_method_2([1, 2, 3, 4])
        
    def test_that_ignore_index_method_2_returns_correct_value(self):
        actual = ignore_index_method_2([1, 2, 3, 4])
        expected = 30
        self.assertEqual(actual, expected)
        actual = ignore_index_method_2([1, 2, 3, 4, 5])
        expected = 60
        self.assertEqual(actual, expected)
        ignore_index_method_2
        
class TestMergeAndSortFunction(TestCase):
    def test_that_merge_and_sort_exist(self):
        merge_and_sort([1, 2, 5, 4], [3, 2, 0, 4])
        
    def test_that_merge_and_sort_returns_correct_value(self):
        actual = merge_and_sort([1, 2, 5, 4], [3, 2, 0, 4])
        expected = [0, 1, 2, 2, 3, 4, 4, 5]
        self.assertEqual(actual, expected)
