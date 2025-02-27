import unittest
from src.seven_segment_display.seven_segment_display import SevenSegmentDisplay

class TestSevenSegmentDisplay(unittest.TestCase):
    ZERO_PROMPT     = "11111101"
    ONE_PROMPT      = "01100001"
    TWO_PROMPT      = "11011011"
    THREE_PROMPT    = "11110011"
    FOUR_PROMPT     = "01100111"
    FIVE_PROMPT     = "10110111"
    SIX_PROMPT      = "10111111"
    SEVEN_PROMPT    = "11100001"
    EIGHT_PROMPT    = "11111111"
    NINE_PROMPT     = "11100111"
    BLANK_PROMPT    = "11110110"

    ZERO = [
        ["#", "#", "#", "#"],
        ["#", " ", " ", "#"],
        ["#", " ", " ", "#"],
        ["#", " ", " ", "#"],
        ["#", "#", "#", "#"], ]

    ONE = [
        [" ", " ", " ", "#"],
        [" ", " ", " ", "#"],
        [" ", " ", " ", "#"],
        [" ", " ", " ", "#"],
        [" ", " ", " ", "#"], ]

    TWO = [
        ["#", "#", "#", "#"],
        [" ", " ", " ", "#"],
        ["#", "#", "#", "#"],
        ["#", " ", " ", " "],
        ["#", "#", "#", "#"], ]

    THREE = [
        ["#", "#", "#", "#"],
        [" ", " ", " ", "#"],
        ["#", "#", "#", "#"],
        [" ", " ", " ", "#"],
        ["#", "#", "#", "#"], ]

    FOUR = [
        ["#", " ", " ", "#"],
        ["#", " ", " ", "#"],
        ["#", "#", "#", "#"],
        [" ", " ", " ", "#"],
        [" ", " ", " ", "#"], ]

    FIVE = [
        ["#", "#", "#", "#"],
        ["#", " ", " ", " "],
        ["#", "#", "#", "#"],
        [" ", " ", " ", "#"],
        ["#", "#", "#", "#"], ]

    SIX = [
        ["#", "#", "#", "#"],
        ["#", " ", " ", " "],
        ["#", "#", "#", "#"],
        ["#", " ", " ", "#"],
        ["#", "#", "#", "#"], ]

    SEVEN = [
        ["#", "#", "#", "#"],
        [" ", " ", " ", "#"],
        [" ", " ", " ", "#"],
        [" ", " ", " ", "#"],
        [" ", " ", " ", "#"], ]

    EIGHT = [
        ["#", "#", "#", "#"],
        ["#", " ", " ", "#"],
        ["#", "#", "#", "#"],
        ["#", " ", " ", "#"],
        ["#", "#", "#", "#"], ]

    NINE = [
        ["#", "#", "#", "#"],
        ["#", " ", " ", "#"],
        ["#", "#", "#", "#"],
        [" ", " ", " ", "#"],
        [" ", " ", " ", "#"], ]

    BLANK = [
        [" ", " ", " ", " "],
        [" ", " ", " ", " "],
        [" ", " ", " ", " "],
        [" ", " ", " ", " "],
        [" ", " ", " ", " "], ]

    def setUp(self):
        self.display = SevenSegmentDisplay()

    def test_display_is_blank_when_blank_prompt_is_given(self):
        self.display.enter_prompt(self.BLANK_PROMPT)
        actual:[[]] = self.display.get_display()
        print(self.display)
        self.assertListEqual(self.BLANK, actual)

    def test_display_is_one_when_one_prompt_is_given(self):
        self.display.enter_prompt(self.ONE_PROMPT)
        actual: [[]] = self.display.get_display()
        print(self.display)
        self.assertListEqual(self.ONE, actual)

    def test_display_is_two_when_two_prompt_is_given(self):
        self.display.enter_prompt(self.TWO_PROMPT)
        actual: [[]] = self.display.get_display()
        print(self.display)
        self.assertListEqual(self.TWO, actual)

    def test_display_is_three_when_three_prompt_is_given(self):
        self.display.enter_prompt(self.THREE_PROMPT)
        actual: [[]] = self.display.get_display()
        print(self.display)
        self.assertListEqual(self.THREE, actual)

    def test_display_is_four_when_four_prompt_is_given(self):
        self.display.enter_prompt(self.FOUR_PROMPT)
        actual: [[]] = self.display.get_display()
        print(self.display)
        self.assertListEqual(self.FOUR, actual)

    def test_display_is_five_when_five_prompt_is_given(self):
        self.display.enter_prompt(self.FIVE_PROMPT)
        actual: [[]] = self.display.get_display()
        print(self.display)
        self.assertListEqual(self.FIVE, actual)

    def test_display_is_six_when_six_prompt_is_given(self):
        self.display.enter_prompt(self.SIX_PROMPT)
        actual: [[]] = self.display.get_display()
        print(self.display)
        self.assertListEqual(self.SIX, actual)

    def test_display_is_seven_when_seven_prompt_is_given(self):
        self.display.enter_prompt(self.SEVEN_PROMPT)
        actual: [[]] = self.display.get_display()
        print(self.display)
        self.assertListEqual(self.SEVEN, actual)

    def test_display_is_eight_when_eight_prompt_is_given(self):
        self.display.enter_prompt(self.EIGHT_PROMPT)
        actual: [[]] = self.display.get_display()
        print(self.display)
        self.assertListEqual(self.EIGHT, actual)

    def test_display_is_nine_when_nine_prompt_is_given(self):
        self.display.enter_prompt(self.NINE_PROMPT)
        actual: [[]] = self.display.get_display()
        print(self.display)
        self.assertListEqual(self.NINE, actual)

    def test_display_is_zero_when_zero_prompt_is_given(self):
        self.display.enter_prompt(self.ZERO_PROMPT)
        actual: [[]] = self.display.get_display()
        print(self.display)
        self.assertListEqual(self.ZERO, actual)