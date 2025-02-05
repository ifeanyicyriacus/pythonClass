from unittest import TestCase
from bank_service.account import Account


class AccountTest(TestCase):
    correct_pin = "0000"
    wrong_pin = "1111"
    empty_pin = ""
    first_name = "first_name"
    last_name = "last_name"
    account_number = 100

    def setUp(self):
        self.bank_account = Account(self.account_number, self.first_name, self.last_name, self.correct_pin)

    def test_account_can_be_created(self):
        # self.assertIsNotNone(self.bank_account)
        self.assertEqual(self.account_number, self.bank_account.account_number())
        self.assertEqual(self.first_name, self.bank_account.get_first_name())
        self.assertEqual(self.last_name, self.bank_account.get_last_name())



