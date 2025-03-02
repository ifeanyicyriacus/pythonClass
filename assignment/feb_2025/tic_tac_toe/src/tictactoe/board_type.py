from enum import Enum
from src.tictactoe.token import Token

class BoardType(Enum):
    EASY = 1
    HARD = 2
    EXTREME = 3
    DANGEROUS = 4

    board:list[list[list[Token]]]

    def __init__(self, difficulty_level:int) -> None:
        self.board = []
        self.difficulty_level = difficulty_level
        match difficulty_level:
            case 1:
                self.board = [
                    [
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY]
                    ],
                ]
            case 2:
                self.board = [
                    [
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY]
                    ],
                ]
            case 3:
                self.board = [
                    [
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY]
                    ],
                    [
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY]
                    ],
                    [
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY]
                    ],
                ]
            case 4:
                self.board = [
                    [
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY],
                    ],
                    [
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY],
                    ],
                    [
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY],
                    ],
                    [
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY],
                        [Token.EMPTY, Token.EMPTY, Token.EMPTY, Token.EMPTY],
                    ]
                ]
            case _:
                raise Exception(f"Invalid difficulty level: {difficulty_level}")

