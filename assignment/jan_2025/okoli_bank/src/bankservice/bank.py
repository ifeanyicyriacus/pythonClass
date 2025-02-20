from src.bankservice.account import Account


class Bank:
    __account_counter = 1
    __accounts: dict[int: Account] = {}

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def get_account_count(self):
        return self.__account_counter

    def generate_account_number(self):
        return str(self.__account_counter)

    def create_account(self, first_name, last_name, pin) -> str:
        account_number = self.generate_account_number()
        new_account = Account(account_number, first_name, last_name, pin)
        self.__accounts[account_number] = new_account
        self.__account_counter += 1
        return account_number

    def get_account_first_name(self, account_number):
        account:Account = self.__accounts.get(account_number)
        return account.first_name

    def get_account_last_name(self, account_number):
        account:Account = self.__accounts.get(account_number)
        return account.last_name

    def check_balance(self, account_number, pin):
        account: Account = self.get_account(account_number)
        return account.check_balance(pin)

    def deposit(self, account_number, amount):
        account: Account = self.get_account(account_number)
        account.deposit(amount)

    def get_account(self, account_number):
        result = self.__accounts.get(account_number)
        if result is None:
            raise ValueError("Account ({}) not found".format(account_number))
        else: return result

    def withdraw(self, account_number, amount, pin):
        account: Account = self.get_account(account_number)
        account.withdraw(amount, pin)

    def transfer(self, sender_account_number, receiver_account_number, amount, sender_pin):
        account_1: Account = self.get_account(sender_account_number)
        account_2: Account = self.get_account(receiver_account_number)
        if account_1 == account_2:
            raise ValueError("You can not transfer between the same account")
        account_1.withdraw(amount, sender_pin)
        account_2.deposit(amount)

    def reset_pin(self, account_number, old_pin, new_pin):
        account: Account = self.get_account(account_number)
        account.update_pin(old_pin, new_pin)

    def update_first_name(self, account_number, new_first_name, pin):
        account: Account = self.get_account(account_number)
        account.update_first_name(new_first_name, pin)

    def update_last_name(self, account_number, new_last_name, correct_pin):
        account: Account = self.get_account(account_number)
        account.update_last_name(new_last_name, correct_pin)
        pass


