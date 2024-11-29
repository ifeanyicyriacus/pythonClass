from unittest import TestCase
from afternoonlatte import multiply_by_two, find_by_length, digit_adder, remove_all_vowels, dict_generator, lists_to_dict, dictionary_to_value_list, update_and_add_to_dict, key_value_swapping

class TestMultiplyByTwoFunction(TestCase):
	def test_that_multiply_by_two_exist(self):
		multiply_by_two([1, 2, 3])
		
	def test_that_number_square_return_correct_value(self):
		actual = multiply_by_two([1, 2, 3])
		expected = [2, 4, 6]
		self.assertEqual(actual, expected)


class TestFindBbyLengthFunction(TestCase):
	def test_that_find_by_length_exist(self):
		find_by_length(["hi", "hello", "why"], 3)
		
	def test_that_find_by_length_return_correct_value(self):
	    actual = find_by_length(["hi", "hello", "why"], 3)
	    expected = ["hello", "why"]
	    self.assertEqual(actual, expected)
	    
class TestDigitAdderFunction(TestCase):
	def test_that_digit_adder_exist(self):
		digit_adder(192374)
		
	def test_that_digit_adder_return_correct_value(self):
	    actual = digit_adder(192374)
	    expected = 26
	    self.assertEqual(actual, expected)
	    
class TestRemoveAllVowelsFunction(TestCase):
    def test_remove_all_vowels_exists(self):
        remove_all_vowels(["Orange", "Apple", "Ice", "Beans", "Rice"])
    
    def test_remove_all_vowels_return_correct_value(self):
        actual = remove_all_vowels(["Orange", "Apple", "Ice", "Beans", "Rice"])
        expected = ["rng", "ppl", "c", "Bns", "Rc"]
        self.assertEqual(actual, expected)
        
class TestDictGeneratorFunction(TestCase):
    def test_dict_generator_exists(self):
        dict_generator()
    
    def test_dict_generator_return_correct_value(self):
        actual = dict_generator()
        expected = {2:4, 4:16, 6:36, 8:64, 10:100}
        self.assertEqual(actual, expected)
        
class TestListsToDictFunction(TestCase):
    def test_that_lists_to_dict_exists(self):
        lists_to_dict([],[])
    
    def test_lists_to_dict_returns_correct_value(self):
        list1 = ["name", "age", "city"]
        list2 = ["Alice", 25, "New York"]
        actual = lists_to_dict(list1, list2)
        expected = {"name":"Alice", "age":25, "city":"New York"}
        self.assertEqual(actual, expected)
        
class TestDictionaryToValueList(TestCase):
    def test_dictionary_to_value_list_exists(self):
        dictionary_to_value_list({})
    
    def test_dictionary_to_value_list_return_correct_value(self):
        sample_dict = {"name":"Alice", "age":25, "city":"New York"}
        actual = dictionary_to_value_list(sample_dict)
        expected = ["Alice", 25, "New York"]
        self.assertEqual(actual, expected)
        
class TestUpdateAndAddToDict(TestCase):
    def test_update_and_add_to_dict_exists(self):
        update_and_add_to_dict({}, {})
    
    def test_dictionary_to_value_list_return_correct_value(self):
        my_dict = {"name":"Alice", "age":25}
        new_dict = {"city":"New York", "age":26}
        actual = update_and_add_to_dict(my_dict, new_dict)
        expected = {"name":"Alice", "age":26, "city":"New York"}
        self.assertEqual(actual, expected)
        

class TestKeyValueSwapping(TestCase):
    def test_key_value_swapping_exists(self):
        key_value_swapping({})
    
    def test_dictionary_to_value_list_return_correct_value(self):
        sample_dict = {"Alice":25, "Bob":26, "Kelven":32}
        actual = key_value_swapping(sample_dict)
        expected = {25:"Alice", 26:"Bob", 32:"Kelven"}
        self.assertEqual(actual, expected)
        



