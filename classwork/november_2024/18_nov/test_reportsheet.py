from unittest import TestCase
from reportsheet import higher_scorer, lowest_scorer

score_sheet_single_highest_and_lowest = [
    ["Ifeanyi", 99, 20, 87, 65], ["James", 54, 19, 87, 70],
	["Daniel", 76, 90, 87, 80],	["Esther", 54, 90, 87, 97],
	["Ogene", 74, 90, 88, 90],	["Ayo", 54, 40, 37, 23],
	["Chris", 54, 97, 47, 66],	["AZed", 80, 90, 80, 21],
	["BiBi", 54, 99, 8, 20],	["Priest", 2, 45, 87, 66]
]
score_sheet_multiple_highest_and_lowest = [
    ["Ifeanyi", 54, 20, 87, 65], ["James", 76, 19, 87, 70],
	["Daniel", 76, 90, 87, 80],	["Esther", 54, 90, 87, 97],
	["Ogene", 74, 90, 87, 90],	["Ayo", 54, 90, 37, 20],
	["Chris", 89, 19, 47, 97],	["AZed", 80, 99, 8, 21],
	["BiBi", 54, 99, 8, 20],	["Priest", 89, 45, 87, 66]
]
score_sheet_with_out_of_range_value = [
    ["Ifeanyi", 54, -10, 87, 65], ["James", 104, 109, 87, 70],
	["Daniel", -1, 90, 87, 80],	["Esther", 54, 90, 87, 97],
	["Ogene", 105, 90, 87, 90],	["Ayo", 101, 90, 37, 20],
	["Chris", 54, 97, 47, 166],	["AZed", 80, 90, 80, 21],
	["BiBi", 54, 99, -8, 20],	["Priest", 89, 45, 87, 66]
]

class TestHighestScorerFunction(TestCase):
    def test_that_it_exist(self):
        higher_scorer([], 0)
        
    def test_that_higher_scorer_return_correct_value_when_there_is_one_highest(self):
        actual = higher_scorer(score_sheet_single_highest_and_lowest, 1)
        expected = [['Ifeanyi'], 99]
        self.assertEqual(actual, expected)
        actual = higher_scorer(score_sheet_single_highest_and_lowest, 2)
        expected = [['BiBi'], 99]
        self.assertEqual(actual, expected)
        actual = higher_scorer(score_sheet_single_highest_and_lowest, 3)
        expected = [['Ogene'], 88]
        self.assertEqual(actual, expected)
        actual = higher_scorer(score_sheet_single_highest_and_lowest, 4)
        expected = [['Esther'], 97]
        self.assertEqual(actual, expected)
        
        
    def test_that_higher_scorer_return_correct_value_when_there_is_multiple_highest(self):
        actual = higher_scorer(score_sheet_multiple_highest_and_lowest, 1)
        expected = [['Chris', 'Priest'], 89]
        self.assertEqual(actual, expected)
        actual = higher_scorer(score_sheet_multiple_highest_and_lowest, 2)
        expected = [['AZed', 'BiBi'], 99]
        self.assertEqual(actual, expected)
        actual = higher_scorer(score_sheet_multiple_highest_and_lowest, 3)
        expected = [['Ifeanyi', 'James', 'Daniel', 'Esther', 'Ogene', 'Priest'], 87]
        self.assertEqual(actual, expected)
        actual = higher_scorer(score_sheet_multiple_highest_and_lowest, 4)
        expected = [['Esther', 'Chris'], 97]
        self.assertEqual(actual, expected)
        
    def test_that_higher_scorer_raises_exception_when_scoresheet_has_out_of_range_values(self):
        self.assertRaises(ValueError, higher_scorer, score_sheet_with_out_of_range_value, 1)
        self.assertRaises(ValueError, higher_scorer, score_sheet_with_out_of_range_value, 2)
        self.assertRaises(ValueError, higher_scorer, score_sheet_with_out_of_range_value, 3)
        self.assertRaises(ValueError, higher_scorer, score_sheet_with_out_of_range_value, 4)
        
class TestLowestScorerFunction(TestCase):
    def test_that_it_exist(self):
        lowest_scorer([], 0)
        
    def test_that_lowest_scorer_return_correct_value_when_there_is_one_highest(self):
        actual = lowest_scorer(score_sheet_single_highest_and_lowest, 1)
        expected = [['Priest'], 2]
        self.assertEqual(actual, expected)
        actual = lowest_scorer(score_sheet_single_highest_and_lowest, 2)
        expected = [['James'], 19]
        self.assertEqual(actual, expected)
        actual = lowest_scorer(score_sheet_single_highest_and_lowest, 3)
        expected = [['BiBi'], 8]
        self.assertEqual(actual, expected)
        actual = lowest_scorer(score_sheet_single_highest_and_lowest, 4)
        expected = [['BiBi'], 20]
        self.assertEqual(actual, expected)
        
        
    def test_that_lowest_scorer_return_correct_value_when_there_is_multiple_highest(self):
        actual = lowest_scorer(score_sheet_multiple_highest_and_lowest, 1)
        expected = [['Ifeanyi', 'Esther', 'Ayo', 'BiBi'], 54]
        self.assertEqual(actual, expected)
        actual = lowest_scorer(score_sheet_multiple_highest_and_lowest, 2)
        expected = [['James', 'Chris'], 19]
        self.assertEqual(actual, expected)
        actual = lowest_scorer(score_sheet_multiple_highest_and_lowest, 3)
        expected = [['AZed', 'BiBi'], 8]
        self.assertEqual(actual, expected)
        actual = lowest_scorer(score_sheet_multiple_highest_and_lowest, 4)
        expected = [['Ayo', 'BiBi'], 20]
        self.assertEqual(actual, expected)
        
    def test_that_lowest_scorer_raises_exception_when_scoresheet_has_out_of_range_values(self):
        self.assertRaises(ValueError, lowest_scorer, score_sheet_with_out_of_range_value, 1)
        self.assertRaises(ValueError, lowest_scorer, score_sheet_with_out_of_range_value, 2)
        self.assertRaises(ValueError, lowest_scorer, score_sheet_with_out_of_range_value, 3)
        self.assertRaises(ValueError, lowest_scorer, score_sheet_with_out_of_range_value, 4)
