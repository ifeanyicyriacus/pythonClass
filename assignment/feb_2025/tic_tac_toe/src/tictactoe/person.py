from src.tictactoe.token import Token


class Person:
    def __init__(self, name:str, token:Token):
        self.name = name
        self.token = token

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name:str):
        self.__name = name

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token:Token):
        self.__token = token
