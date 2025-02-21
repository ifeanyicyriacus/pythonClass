import unittest
from src.diary_services.entry import Entry

class EntryTestCase(unittest.TestCase):
    entry:Entry = None
    entry_id = 0
    title = 'Entry Title'
    body = 'body'

    def setUp(self):
        self.entry = Entry(self.entry_id, self.title, self.body)

    def test_entry_can_be_created(self):
        self.assertEqual(self.entry.entry_id, self.entry_id)
        self.assertEqual(self.entry.title, self.title)
        self.assertEqual(self.entry.body, self.body)
        self.assertFalse(self.entry.date_created == "")

    def test_entry_title_can_be_updated(self):
        self.assertEqual(self.entry_id, self.entry.entry_id)
        self.assertEqual(self.title, self.entry.title)
        new_title = 'New Entry Title'
        self.entry.update_title(new_title)
        self.assertNotEqual(self.title, self.entry.title)
        self.assertEqual(new_title, self.entry.title)
        self.assertEqual(self.entry_id, self.entry.entry_id)

    def test_entry_body_can_be_updated(self):
        self.assertEqual(self.entry_id, self.entry.entry_id)
        self.assertEqual(self.body, self.entry.body)
        new_body = 'New Entry Body'
        self.entry.update_body(new_body)
        self.assertNotEqual(self.body, self.entry.body)
        self.assertEqual(new_body, self.entry.body)
        self.assertEqual(self.entry_id, self.entry.entry_id)

    def test_entry_body_cannot_be_updated_with_empty_body(self):
        self.assertEqual(self.body, self.entry.body)
        self.assertRaises(ValueError, self.entry.update_body, "")
        self.assertEqual(self.body, self.entry.body)

    def test_entry_title_cannot_be_updated_with_empty_title(self):
        self.assertEqual(self.title, self.entry.title)
        self.assertRaises(ValueError, self.entry.update_title, "")
        self.assertEqual(self.title, self.entry.title)

    def test_entry_to_string_displays_the_overwritten_format(self):
        self.assertTrue(str(self.entry).find("(0)\tEntry Title") != -1)