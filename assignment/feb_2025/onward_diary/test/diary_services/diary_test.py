import unittest

from src.diary_services.diary import Diary

class DiaryTestCase(unittest.TestCase):
    dairy:Diary = None
    usernames:list = ["username1", "username2", "username3"]
    passwords:list = ["password1", "password2", "password3"]
    wrong_password = "wrong password"
    titles:list[str] = ["title1", "title2", "title3"]
    bodies:list[str] = ["entry1", "entry2", "entry3"]
    validIds:list[int] = [1, 2]
    invalidId = 100
    valid_ids = [1, 2]
    invalid_ids = [100]
    empty = ""

    def setUp(self):
        self.diary:Diary = Diary(self.usernames[0], self.passwords[0])
        self.diary.unlock(self.passwords[0])

    def test_diary_is_created_without_any_entry(self):
        self.assertEqual(0, self.diary.number_of_entries)
        self.assertEqual({}, self.diary.entries)

    def test_diary_can_not_be_created_with_empty_or_null_username_or_password(self):
        self.assertRaises(ValueError, Diary, self.passwords[0], None)
        self.assertRaises(ValueError, Diary, self.empty, self.passwords[0])
        self.assertRaises(ValueError, Diary, None, self.passwords[0])
        self.assertRaises(ValueError, Diary, self.usernames[0], self.empty)

    def test_diary_can_be_unlocked(self):
        correct_password:str = self.passwords[0]
        self.diary.lock()
        self.assertTrue(self.diary.is_locked)
        self.diary.unlock(correct_password)
        self.assertFalse(self.diary.is_locked)

    def test_diary_can_not_be_unlocked_with_wrong_password(self):
        self.diary.lock()
        self.assertRaises(ValueError, self.diary.unlock, self.wrong_password)

    # def test_diary_can_not_perform_any_operation_if_diary_is_locked(self):
    #     self.diary.create_entry(self.titles[0], self.bodies[0])
    #     self.assertEqual(1, self.diary.number_of_entries)
    #     self.diary.lock()

    def test_diary_can_be_locked(self):
        self.assertFalse(self.diary.is_locked)
        self.diary.lock()
        self.assertTrue(self.diary.is_locked)

    def test_diary_can_not_perform_CRUD_operations_if_locked(self):
        self.diary.lock()
        self.assertTrue(self.diary.is_locked)
        self.assertEqual(0, self.diary.number_of_entries)
        self.assertRaises(ValueError, self.diary.create_entry, self.titles[0], self.bodies[0])
        self.assertEqual(0, self.diary.number_of_entries)

    def test_diary_can_not_create_entry_if_diary_is_unlocked(self):
        self.assertFalse(self.diary.is_locked)
        self.assertEqual(0, self.diary.number_of_entries)
        self.diary.create_entry(self.titles[0], self.bodies[0])
        self.assertEqual(1, self.diary.number_of_entries)
        self.diary.create_entry(self.titles[1], self.bodies[1])
        self.assertEqual(2, self.diary.number_of_entries)
        for index in range(2):
            self.assertEqual(self.titles[index], self.diary.find_entry_by_id(self.valid_ids[index]).title)
            self.assertEqual(self.bodies[index], self.diary.find_entry_by_id(self.valid_ids[index]).body)


    def test_diary_raises_exception_if_no_entry_match_id_if_diary_is_unlocked(self):
        self.assertEqual(0, self.diary.number_of_entries)
        self.








