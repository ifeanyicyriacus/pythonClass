class Account:

    def __init__(self, account_number, first_name, last_name, pin):
        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        self._pin = pin
        self._balance = 0

    @property
    def _balance(self):
        return self.__balance

    @_balance.setter
    def _balance(self, value):
        self.__balance = value

    def check_balance(self, pin):
        if self._confirm_pin(pin):
            return self._balance
        else: raise ValueError('Pin is incorrect')

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        if first_name is None or first_name == '':
            raise ValueError('First name cannot be empty')
        self.__first_name = first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        if last_name is None or last_name == '':
            raise ValueError('Last name cannot be empty')
        self.__last_name = last_name

    @property
    def account_number(self) -> int:
        return self.__account_number

    @account_number.setter
    def account_number(self, account_number):
        if account_number is None or account_number == 0:
            raise ValueError('Account number cannot be zero')
        self.__account_number = account_number

    @property
    def _pin(self) -> str:
        return self.__pin

    @_pin.setter
    def _pin(self, pin):
        if pin is None or pin == '':
            raise ValueError('Pin cannot be empty')
        self.__pin = pin

    def update_first_name(self, first_name, pin):
        if first_name is None or first_name == '' or pin is None or pin == '':
            raise ValueError('First name or pin cannot be empty')
        if  not (pin == self._pin):
            raise ValueError('Pin is incorrect')
        self.first_name = first_name

    def update_last_name(self, last_name, pin):
        if last_name is None or last_name == '' or pin is None or pin == '':
            raise ValueError('Last name or pin cannot be empty')
        if self._confirm_pin(pin):
            self.last_name = last_name
        else: raise ValueError('Pin is incorrect')


    def _confirm_pin(self, pin) -> bool:
        return self._pin == pin

    def update_pin(self, old_pin:str, new_pin:str):
        if new_pin is None or new_pin == '':
            raise ValueError('New pin field cannot be empty')
        if self._confirm_pin(old_pin):
            self._pin = new_pin
        else: raise ValueError('Current pin is incorrect')

    def deposit(self, amount:float):
        if amount < 0: raise ValueError('Amount cannot be negative')
        self._balance += amount

    def withdraw(self, amount:float, pin:str):
        if not self._confirm_pin(pin): raise ValueError('Pin is incorrect')
        if amount < 0: raise ValueError('Amount cannot be negative')
        if amount > self._balance: raise ValueError('Amount cannot be greater than balance')
        self._balance -= amount


