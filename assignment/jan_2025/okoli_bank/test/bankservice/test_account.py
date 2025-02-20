from unittest import TestCase
from src.bankservice.account import Account

class AccountTest(TestCase):
    correct_pin = "0000"
    updated_pin = "2222"
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

    def test_account_raises_error_when_manipulating_profile_detail_using_incorrectPin(self):
        self.assertEqual(self.first_name, self.bank_account.first_name)
        self.assertRaises(ValueError, self.bank_account.update_first_name, self.updated_first_name, self.wrong_pin)
        self.assertEqual(self.first_name, self.bank_account.first_name)

        self.assertEqual(self.last_name, self.bank_account.last_name)
        self.assertRaises(ValueError, self.bank_account.update_last_name, self.updated_last_name, self.wrong_pin)
        self.assertEqual(self.last_name, self.bank_account.last_name)

    def test_account_balance_is_initialized_to_zero(self):
        self.assertEqual(self.ZERO, self.bank_account.check_balance(self.correct_pin))

    def test_account_pin_can_not_be_updated_when_the_old_pin_is_incorrect(self):
        self.assertRaises(ValueError, self.bank_account.update_pin, self.wrong_pin, self.updated_pin)

    def test_account_pin_can_be_updated_when_correct_pin_is_given(self):
        self.assertEqual(self.ZERO, self.bank_account.check_balance(self.correct_pin))
        self.assertRaises(ValueError, self.bank_account.check_balance, self.updated_pin)
        self.bank_account.update_pin(self.correct_pin, self.updated_pin)
        self.assertRaises(ValueError, self.bank_account.check_balance, self.correct_pin)
        self.assertEqual(self.ZERO, self.bank_account.check_balance(self.updated_pin))

    def test_account_can_only_check_balance_when_pin_is_correct(self):
        self.assertRaises(ValueError, self.bank_account.check_balance, self.wrong_pin)
        self.assertEqual(self.ZERO, self.bank_account.check_balance(self.correct_pin))

    def test_account_support_balance_increase(self):
        self.bank_account.deposit(30_000)
        self.assertEqual(30_000, self.bank_account.check_balance(self.correct_pin))
        self.bank_account.deposit(300)
        self.bank_account.deposit(400)
        self.assertEqual(30_700, self.bank_account.check_balance(self.correct_pin))

    def test_account_raises_exception_for_invalid_increase_amount(self):
        self.assertRaises(ValueError, self.bank_account.deposit, -300)
        self.assertEqual(0, self.bank_account.check_balance(self.correct_pin))

    def test_account_supports_withdrawal(self):
        self.bank_account.deposit(30_000)
        self.assertEqual(30_000, self.bank_account.check_balance(self.correct_pin))
        self.bank_account.withdraw(10_000, self.correct_pin)
        self.assertEqual(20_000, self.bank_account.check_balance(self.correct_pin))

    def test_account_raises_exception_for_invalid_withdrawal_amount(self):
        self.bank_account.deposit(50_000)
        self.assertEqual(50_000, self.bank_account.check_balance(self.correct_pin))
        self.assertRaises(ValueError, self.bank_account.withdraw, -300, self.correct_pin)
        self.assertRaises(ValueError, self.bank_account.withdraw, 100_000, self.correct_pin)
        self.assertEqual(50_000, self.bank_account.check_balance(self.correct_pin))

    def test_account_raisesException_for_withdrawal_with_incorrect_pin(self):
        self.bank_account.deposit(10_000)
        self.assertRaises(ValueError, self.bank_account.withdraw, 1_300, self.wrong_pin)
        self.assertEqual(10_000, self.bank_account.check_balance(self.correct_pin))
