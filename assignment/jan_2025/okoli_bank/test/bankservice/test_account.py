from unittest import TestCase
from src.bankservice.account import Account

class AccountTest(TestCase):
    correct_pin = "0000"
    wrong_pin = "1111"
    first_name = "first_name"
    updated_first_name = "updated_first_name"
    last_name = "last_name"
    updated_last_name = "updated_last_name"
    account_number = 100
    empty_string = ""
    ZERO = 0

    def setUp(self):
        self.bank_account = Account(self.account_number, self.first_name, self.last_name, self.correct_pin)

    def test_account_can_be_created(self):
        self.assertIsNotNone(self.bank_account)
        self.assertEqual(self.account_number, self.bank_account.account_number)
        self.assertEqual(self.first_name, self.bank_account.first_name)
        self.assertEqual(self.last_name, self.bank_account.last_name)

    def test_account_can_be_created_only_with_legal_value(self):
        self.assertRaises(ValueError, Account, self.ZERO, self.first_name, self.last_name, self.correct_pin)
        self.assertRaises(ValueError, Account, self.account_number, self.empty_string, self.last_name, self.correct_pin)
        self.assertRaises(ValueError, Account, self.account_number, self.first_name, self.empty_string, self.correct_pin)
        self.assertRaises(ValueError, Account, self.account_number, self.first_name, self.last_name, self.empty_string)

    def test_account_first_name_detail_can_be_updated(self):
        self.assertEqual(self.first_name, self.bank_account.first_name)
        self.bank_account.update_first_name(self.updated_first_name, self.correct_pin)
        self.assertEqual(self.updated_first_name, self.bank_account.first_name)

    def test_account_last_name_detail_can_be_updated(self):
        self.assertEqual(self.last_name, self.bank_account.last_name)
        self.bank_account.last_name = self.updated_last_name
        self.assertEqual(self.updated_last_name, self.bank_account.last_name)

