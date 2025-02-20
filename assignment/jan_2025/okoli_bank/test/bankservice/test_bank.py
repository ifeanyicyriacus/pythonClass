from unittest import TestCase

from src.bankservice.bank import Bank

first_names = ["John", "Ifeanyi"]
last_names = ["Doe", "Mark"]
pins = ["1234", "0000"]


class TestBank(TestCase):

    def setUp(self):
        self.bank = Bank("Fidelity Bank Plc")

    def test_init(self):
        self.assertIsInstance(self.bank, Bank)
        self.assertEqual("Fidelity Bank Plc", self.bank.name)

    def test_bank_can_create_account(self):
        self.assertEqual(1, self.bank.get_account_count())
        account_number = self.bank.create_account(first_names[0], last_names[0], pins[0])
        self.assertEqual(first_names[0], self.bank.get_account_first_name(account_number))
        self.assertEqual(last_names[0], self.bank.get_account_last_name(account_number))
        self.assertEqual(0, self.bank.check_balance(account_number, pins[0]))
        self.assertEqual(2, self.bank.get_account_count())

    def test_bank_can_deposit_into_account(self):
        account_number_1 = self.bank.create_account(first_names[0], last_names[0], pins[0])
        self.bank.deposit(account_number_1, 100_000)
        self.assertEqual(100_000, self.bank.check_balance(account_number_1, pins[0]))
        account_number_2 = self.bank.create_account(first_names[1], last_names[1], pins[1])
        self.bank.deposit(account_number_2, 150_000)
        self.assertEqual(150_000, self.bank.check_balance(account_number_2, pins[1]))

    def test_bank_can_withdraw_from_account_when_balance_is_more_than_the_amount(self):
        pin = pins[0]
        account_number = self.bank.create_account(first_names[0], last_names[0], pin)
        self.bank.deposit(account_number, 10_000)
        self.assertEqual(10_000, self.bank.check_balance(account_number, pin))
        self.bank.withdraw(account_number, 9_000, pin)
        self.assertEqual(1_000, self.bank.check_balance(account_number, pin))

    def test_bank_can_transfer_money_from_account_to_account(self):
        pin1 = pins[0]
        pin2 = pins[1]
        account_number_1 = self.bank.create_account(first_names[0], last_names[0], pin1)
        account_number_2 = self.bank.create_account(first_names[1], last_names[1], pin2)

        self.bank.deposit(account_number_1, 150_000)
        self.assertEqual(150_000, self.bank.check_balance(account_number_1, pin1))
        self.assertEqual(0, self.bank.check_balance(account_number_2, pin2))

        self.bank.transfer(account_number_1, account_number_2, 50_000, pin1)
        self.assertEqual(100_000, self.bank.check_balance(account_number_1, pin1))
        self.assertEqual(50_000, self.bank.check_balance(account_number_2, pin2))

        self.bank.transfer(account_number_2, account_number_1, 5_000, pin2)
        self.assertEqual(45_000, self.bank.check_balance(account_number_2, pin2))
        self.assertEqual(105_000, self.bank.check_balance(account_number_1, pin1))

    def test_bank_transfer_reverts_money_sender_pin_is_wrong(self):
        pin1 = pins[0]
        pin2 = pins[1]
        incorrect_sender_pin = "incorrect"
        account_number_1 = self.bank.create_account(first_names[0], last_names[0], pin1)
        account_number_2 = self.bank.create_account(first_names[1], last_names[1], pin2)

        self.bank.deposit(account_number_1, 150_000)
        self.assertEqual(150_000, self.bank.check_balance(account_number_1, pin1))
        self.assertEqual(0, self.bank.check_balance(account_number_2, pin2))

        self.assertRaises(ValueError, self.bank.transfer, account_number_1, account_number_2, 50_000,
                          incorrect_sender_pin)
        self.assertEqual(150_000, self.bank.check_balance(account_number_1, pin1))
        self.assertEqual(0, self.bank.check_balance(account_number_2, pin2))

    def test_bank_transfer_reverts_money_when_sender_account_number_is_incorrect(self):
        correct_sender_pin = pins[0]
        correct_receiver_pin = pins[1]

        sender_account_number = self.bank.create_account(first_names[0], last_names[0], correct_sender_pin)
        receiver_account_number = self.bank.create_account(first_names[1], last_names[1], correct_receiver_pin)
        incorrect_sender_account_number = 0

        self.bank.deposit(sender_account_number, 150_000)
        self.assertEqual(150_000, self.bank.check_balance(sender_account_number, correct_sender_pin))
        self.assertEqual(0, self.bank.check_balance(receiver_account_number, correct_receiver_pin))

        self.assertRaises(ValueError,
                          self.bank.transfer, incorrect_sender_account_number, receiver_account_number, 50_000,
                                             correct_sender_pin)
        self.assertEqual(150_000, self.bank.check_balance(sender_account_number, correct_sender_pin))
        self.assertEqual(0, self.bank.check_balance(receiver_account_number, correct_receiver_pin))

    def test_bank_transfer_reverts_money_when_receiver_account_number_is_incorrect(self):
        correct_sender_pin = pins[0]
        correct_receiver_pin = pins[1]

        sender_account_number = self.bank.create_account(first_names[0], last_names[0], correct_sender_pin)
        receiver_account_number = self.bank.create_account(first_names[1], last_names[1], correct_receiver_pin)
        incorrect_receiver_account_number = 0

        self.bank.deposit(sender_account_number, 150_000)
        self.assertEqual(150_000, self.bank.check_balance(sender_account_number, correct_sender_pin))
        self.assertEqual(0, self.bank.check_balance(receiver_account_number, correct_receiver_pin))

        self.assertRaises(ValueError,
                          self.bank.transfer, sender_account_number, incorrect_receiver_account_number, 50_000,
                                             correct_sender_pin)
        self.assertEqual(150_000, self.bank.check_balance(sender_account_number, correct_sender_pin))
        self.assertEqual(0, self.bank.check_balance(receiver_account_number, correct_receiver_pin))

    def test_bank_transfer_revert_to_original_state_when_sender_balance_is_less_than_the_amount(self):
        correct_sender_pin = pins[0]
        correct_receiver_pin = pins[1]

        sender_account_number = self.bank.create_account(first_names[0], last_names[0], correct_sender_pin)
        receiver_account_number = self.bank.create_account(first_names[1], last_names[1], correct_receiver_pin)

        self.bank.deposit(sender_account_number, 150_000)
        self.assertEqual(150_000, self.bank.check_balance(sender_account_number, correct_sender_pin))
        self.assertEqual(0, self.bank.check_balance(receiver_account_number, correct_receiver_pin))

        self.assertRaises(ValueError, self.bank.transfer, sender_account_number, receiver_account_number, 500_000, correct_sender_pin)
        self.assertEqual(150_000, self.bank.check_balance(sender_account_number, correct_sender_pin))
        self.assertEqual(0, self.bank.check_balance(receiver_account_number, correct_receiver_pin))


    def test_bank_transfer_between_the_same_account_throw_exception(self):
        correct_sender_pin = pins[0]
        sender_account_number = self.bank.create_account(first_names[0], last_names[0], correct_sender_pin)
        self.bank.deposit(sender_account_number, 150_000)
        self.assertEqual(150_000, self.bank.check_balance(sender_account_number, correct_sender_pin))
        self.assertRaises(ValueError, self.bank.transfer, sender_account_number, sender_account_number,50_000, correct_sender_pin)
        self.assertEqual(150_000, self.bank.check_balance(sender_account_number, correct_sender_pin))

    def test_bank_can_change_account_pin(self):
        correct_pin = pins[0]
        new_pin = pins[1]
        account_number = self.bank.create_account(first_names[0], last_names[0], correct_pin)
        self.bank.deposit(account_number, 75_000)
        self.bank.reset_pin(account_number, correct_pin, new_pin)
        self.assertEqual(75_000, self.bank.check_balance(account_number, new_pin))

    def test_bank_can_change_account_first_name(self):
        correct_pin = pins[0]
        new_first_name = first_names[1]
        account_number = self.bank.create_account(first_names[0], last_names[0], correct_pin)
        self.bank.update_first_name(account_number, new_first_name, correct_pin)
        self.assertEqual(new_first_name, self.bank.get_account_first_name(account_number))

    def test_bank_can_change_account_last_name(self):
        correct_pin = pins[0]
        new_last_name = last_names[1]
        account_number = self.bank.create_account(first_names[0], last_names[0], correct_pin)
        self.bank.update_last_name(account_number, new_last_name, correct_pin)
        self.assertEqual(new_last_name, self.bank.get_account_last_name(account_number))
