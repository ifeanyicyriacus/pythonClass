from src.tictactoe.token import Token
from src.tictactoe.person import Person
from tictactoe.board_type import BoardType


class TicTacToeGame:

    def __init__(self, no_of_players:int, difficulty_level:int):
        self.no_of_players = no_of_players
        self.difficulty_level = difficulty_level

        # self.players:list[Person] =
        self.GAME_BOARD:list[list[list[Token]]] = BoardType(difficulty_level).board


    def start_game(self):
        pass