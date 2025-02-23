import unittest

from src.diary_services.diary import Diary

class DiaryTestCase(unittest.TestCase):
    dairy:Diary = None
    usernames:list = ["username1", "username2", "username3"]
    passwords:list = ["password1", "password2", "password3"]
    wrong_password = "wrong password"
    titles:list[str] = ["title1", "title2", "title3"]
    bodies:list[str] = ["entry1", "entry2", "entry3"]
    invalid_id = 100
    valid_ids = [1, 2]
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

    def test_diary_can_not_be_unlocked_with_empty_password(self):
        self.diary.lock()
        self.assertRaises(ValueError, self.diary.unlock, self.empty)
        self.assertRaises(ValueError, self.diary.unlock, None)


    def test_diary_can_not_perform_any_operation_if_diary_is_locked(self):
        self.diary.create_entry(self.titles[0], self.bodies[0])
        self.assertEqual(1, self.diary.number_of_entries)
        self.diary.lock()

        self.assertRaises(ValueError, self.diary.create_entry, self.titles[1], self.bodies[1])
        self.assertRaises(ValueError, self.diary.update_entry, self.valid_ids[0], self.titles[0], self.bodies[0])
        self.assertRaises(ValueError, self.diary.find_entry_by_id, self.valid_ids[0])
        self.assertRaises(ValueError, self.diary.delete, self.valid_ids[0])
        self.assertRaises(ValueError, self.diary.change_password, self.passwords[1], self.passwords[0])
        self.assertRaises(ValueError, self.diary.change_username, self.usernames[1], self.passwords[0])

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
        self.diary.create_entry(self.titles[0], self.bodies[0])
        self.assertEqual(1, self.diary.number_of_entries)
        self.assertRaises(ValueError, self.diary.find_entry_by_id, self.invalid_id)

    def test_diary_can_delete_entry(self):
        self.assertEqual(0, self.diary.number_of_entries)
        self.diary.create_entry(self.titles[0], self.bodies[0])
        self.assertEqual(1, self.diary.number_of_entries)
        self.assertEqual(self.titles[0], self.diary.find_entry_by_id(self.valid_ids[0]).title)
        self.assertEqual(self.bodies[0], self.diary.find_entry_by_id(self.valid_ids[0]).body)
        self.diary.delete(self.valid_ids[0])
        self.assertEqual(0, self.diary.number_of_entries)
        self.assertRaises(ValueError, self.diary.find_entry_by_id, self.valid_ids[0])

    def test_diary_raises_exception_when_trying_to_delete_entry_that_does_not_exist(self):
        self.assertEqual(0, self.diary.number_of_entries)
        self.diary.create_entry(self.titles[0], self.bodies[0])
        self.assertEqual(1, self.diary.number_of_entries)
        self.assertRaises(ValueError, self.diary.delete, self.invalid_id)
        self.assertEqual(1, self.diary.number_of_entries)

    def test_diary_can_update_entry(self):
        self.assertEqual(0, self.diary.number_of_entries)
        self.diary.create_entry(self.titles[0], self.bodies[0])
        self.assertEqual(1, self.diary.number_of_entries)
        self.assertEqual(self.titles[0], self.diary.find_entry_by_id(self.valid_ids[0]).title)
        self.assertEqual(self.bodies[0], self.diary.find_entry_by_id(self.valid_ids[0]).body)
        self.diary.update_entry(self.valid_ids[0], self.titles[1], self.bodies[1])
        self.assertEqual(1, self.diary.number_of_entries)
        self.assertEqual(self.titles[1], self.diary.find_entry_by_id(self.valid_ids[0]).title)
        self.assertEqual(self.bodies[1], self.diary.find_entry_by_id(self.valid_ids[0]).body)

    def test_diary_throw_exception_when_trying_to_update_entry_that_does_not_exist(self):
        self.assertEqual(0, self.diary.number_of_entries)
        self.assertRaises(ValueError, self.diary.update_entry, self.invalid_id, self.titles[1], self.bodies[1])

    def test_diary_can_change_username_when_diary_correct_password_is_given(self):
        self.assertEqual(self.usernames[0], self.diary.username)
        self.diary.change_username(self.usernames[1], self.passwords[0])
        self.assertEqual(self.usernames[1], self.diary.username)

    def test_diary_can_not_change_username_when_incorrect_password_is_given(self):
        self.assertEqual(self.usernames[0], self.diary.username)
        self.assertRaises(ValueError, self.diary.change_username, self.usernames[1], self.wrong_password)
        self.assertNotEqual(self.usernames[1], self.diary.username)

    def test_diary_can_change_password_when_correct_password_is_given(self):
        old_password = self.passwords[0]
        new_password = self.passwords[1]
        self.diary.change_password(new_password, old_password)

    def test_diary_cannot_change_password_when_incorrect_password_is_given(self):
        old_password = self.passwords[0]
        new_password = self.passwords[1]
        self.diary.change_password(new_password, old_password)
        self.assertRaises(ValueError, self.diary.change_password, new_password, self.wrong_password)
        self.diary.change_username(self.usernames[1], new_password)
        self.assertEqual(self.usernames[1], self.diary.username)

    def test_diary_to_string_displays_the_overwritten_format(self):
        count = 1; splits = 2
        while count <=  3:
            self.diary.create_entry(self.titles[0], self.bodies[0])
            self.assertEqual(len(str(self.diary).split("title")), splits)
            count += 1; splits += 1


