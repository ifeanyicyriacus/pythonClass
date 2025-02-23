import unittest

from src.diary_services.diary import Diary
from src.diary_services.diaries import Diaries

class DiariesTestCase(unittest.TestCase):
    diaries:Diaries
    emptyField = ""
    username1 = "username1"
    password1 = "password1"
    username2 = "username2"
    password2 = "password2"
    unknownUsername = "username3"
    unknownPassword = "password3"

    def setUp(self):
        self.diaries = Diaries()

    def test_diaries_can_add_diary_with_valid_input(self):
        self.assertEqual(0, self.diaries.size())
        self.diaries.add(self.username1, self.password1)
        self.assertEqual(1, self.diaries.size())
        self.diaries.add(self.username2, self.password2)
        self.assertEqual(2, self.diaries.size())

    def test_diaries_can_not_add_diary_if_username_or_password_is_empty_and_throws_exception(self):
        empty_field = self.emptyField
        username = self.username1
        password = self.password1

        self.assertEqual(0, self.diaries.size())
        self.assertRaises(ValueError, self.diaries.add, empty_field, password)
        self.assertRaises(ValueError, self.diaries.add, username, empty_field)
        self.assertRaises(ValueError, self.diaries.add, empty_field, empty_field)

    def test_diaries_can_find_diary_by_username(self):
        self.assertEqual(0, self.diaries.size())
        self.diaries.add(self.username1, self.password1)
        self.diaries.add(self.username2, self.password2)
        self.assertEqual(2, self.diaries.size())
        diary:Diary = self.diaries.find_by_username(self.username1)
        self.assertEqual(self.username1, diary.username)
        diary = self.diaries.find_by_username(self.username2)
        self.assertEqual(self.username2, diary.username)

    def test_diaries_find_diary_by_username_throws_exception_if_username_is_not_present(self):
        self.assertRaises(ValueError, self.diaries.find_by_username, self.unknownUsername)
        self.assertRaises(ValueError, self.diaries.find_by_username, self.emptyField)

    def test_diaries_can_delete_diary(self):
        self.assertEqual(0, self.diaries.size())
        self.diaries.add(self.username1, self.password1)
        self.diaries.add(self.username2, self.password2)
        self.assertEqual(2, self.diaries.size())
        self.diaries.delete(self.username1, self.password1)
        self.assertEqual(1, self.diaries.size())
        self.assertRaises(ValueError, self.diaries.find_by_username, self.username1)

    def test_diaries_can_not_delete_diary_with_incorrect_credentials(self):
        self.assertEqual(0, self.diaries.size())
        self.diaries.add(self.username1, self.password1)
        self.diaries.add(self.username2, self.password2)
        self.assertEqual(2, self.diaries.size())

        self.assertRaises(ValueError, self.diaries.delete, self.unknownUsername, self.unknownPassword)
        self.assertRaises(ValueError, self.diaries.delete, self.unknownUsername, self.password1)
        self.assertRaises(ValueError, self.diaries.delete, self.username1, self.unknownPassword)
        self.assertEqual(2, self.diaries.size())

    def test_diaries_can_not_add_diary_if_username_is_already_present(self):
        self.assertEqual(0, self.diaries.size())
        self.diaries.add(self.username1, self.password1)
        self.assertRaises(ValueError, self.diaries.add, self.username1, self.password1)
