class Account:

    def __init__(self, account_number, first_name, last_name, pin):
        self.__account_number = account_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__pin = pin

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

    def account_number(self) -> int:
        return self.__account_number

    def pin(self, pin):
        if pin is None or pin == '':
            raise ValueError('Pin cannot be empty')
        self.__pin = pin

