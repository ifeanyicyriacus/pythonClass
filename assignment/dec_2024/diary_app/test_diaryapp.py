from unittest import TestCase
from entry import Entry
from diary import Diary

class TestEntryClass(TestCase):
    def test_that_entry_class_exist(self):
        Entry
    
    def test_that_entry_constructor_creates_a_new_entry(self):
        entry_count_before_instantiation = Entry.entry_count()
        new_entry_subject = "Dec 15 entry"
        new_entry_body = "They sent the wrong santa to Semicolon, he comes bearing snacks :)"
        new_entry = Entry(new_entry_subject, new_entry_body)
        
        self.assertEqual(new_entry.ID, (entry_count_before_instantiation + 1));
        self.assertEqual(new_entry.entry_subject, new_entry_subject);
        self.assertEqual(new_entry.entry_body, new_entry_body);
        self.assertEqual(Entry.entry_count(), (entry_count_before_instantiation + 1));
        

class TestDiaryClass(TestCase):
    def test_that_diary_class_exist(self):
        Diary
        
    def test_diary_constructor_creates_a_new_diary(self):
        diary_count_before_instantiation = Diary.diary_count()
        diary_name = "Business"
        new_diary = Diary(diary_name)
        self.assertEqual(new_diary.name, diary_name)
        self.assertEqual(new_diary.entries, [])
        self.assertEqual(Diary.diary_count(), diary_count_before_instantiation + 1)
        
    def test_that_you_can_not_add_to_entry_when_diary_is_locked(self):
        diary_name = "Personal Reflection"
        new_diary = Diary(diary_name)
        subject = "Time and Money"
        body = "I think money or its abstraction should be a fundamental quantity like mass and time"
        self.assertIsNone(new_diary.add_entry(subject, body))
        
    def test_that_you_can_add_to_entry_when_diary_is_locked(self):
        diary_name = "Personal Reflection"
        new_diary = Diary(diary_name)
        subject = "Time and Money"
        body = "I think money or its abstraction should be a fundamental quantity like mass and time"
        new_diary.is_locked = False
        new_diary.add_entry(subject, body)
        new_diary.add_entry(subject, body)
        self.assertIsNotNone(new_diary.add_entry(subject, body))
        self.assertEqual(len(new_diary.entries), 3)
        
    def test_that_find_entry_by_id_returns_correct_value(self):
        diary_name = "Dietel Old Testament"
        new_diary = Diary(diary_name)
        new_diary.is_locked = False
        actual_1 = new_diary.add_entry("Mathematics", "What you cant measure dont exist")
        actual_2 = new_diary.add_entry("Computer Science", "It all boils down to zeros(0) and Ones(1)")
        expected_1 = new_diary.find_entry_by_id(actual_1.ID)
        expected_2 = new_diary.find_entry_by_id(actual_2.ID)
        self.assertEqual(actual_1, expected_1)
        self.assertEqual(actual_2, expected_2)
        
    def test_that_delete_entry_function_works(self):
        diary_name = "Joke Collection"
        new_diary = Diary(diary_name)
        new_diary.is_locked = False
        entry1 = new_diary.add_entry("Kevin Hart", "JUMANJI Director cut")
        entry2 = new_diary.add_entry("Chris Rock", "Everybody loves Chris")
        no_of_entries_before_deletion = len(new_diary.entries)
        
        new_diary.delete_entry(new_diary.find_entry_by_id(entry1.ID))
        new_diary.delete_entry(new_diary.find_entry_by_id(entry2.ID))
        no_of_entries_after_deletion = len(new_diary.entries)
        
        self.assertNotEqual(no_of_entries_before_deletion, no_of_entries_after_deletion)
        self.assertEqual((no_of_entries_before_deletion - 2), no_of_entries_after_deletion)
        
        
