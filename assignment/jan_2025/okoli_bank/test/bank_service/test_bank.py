from unittest import TestCase
from bank_service import account as Account


    def test_something(self):
        self.assertEqual(True, False)  # add assertion here





class Diary:
    _diary_count = 0

    def __init__(self, name: str):
        Diary._diary_count += 1
        self.name = name
        self.is_locked = True
        self.entries = []

    def diary_count() -> int:
        return Diary._diary_count

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name