from unittest import TestCase

from task.breakfast import breakfast


class Test(TestCase):
    def test_breakfast(self):
        actual = breakfast("abcde", "cdeab")
        expected = True
        self.assertEqual(actual, expected)

        actual = breakfast("cba", "abc")
        expected = False
        self.assertEqual(actual, expected)

        actual = breakfast("13456", "45613")
        expected = True
        self.assertEqual(actual, expected)

        actual = breakfast("ab", "ba")
        expected = True
        self.assertEqual(actual, expected)

        actual = breakfast("12", "31")
        expected = False
        self.assertEqual(actual, expected)
