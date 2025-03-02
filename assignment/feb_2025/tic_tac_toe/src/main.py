from tictactoe.tic_tac_toe_game import TicTacToeGame


class Main:
    def main(self) -> None:
        print("Welcome to Dynamite Tic-Tac-Toe Game")
        self.select_game_mode()
        print("GAME OVER")

    def select_game_mode(self) -> bool:
        game_mode_menu = """
        Choose Game Mode:
        1. Single Player - CPU Clash:
           Defend the human dignity!
        2. Two Player - Tic-Tac-Toe Takedown:
           Challenge your fellow mortal!
        0. Exit ->|
            Quit the game (but why would you want to?)
        """

        game_on = True
        while game_on:
            game_mode_choice = input(game_mode_menu)
            match game_mode_choice:
                case "1": 
                    game_on = self.select_difficulty_level(int(game_mode_choice))
                case "2": 
                    game_on = self.select_difficulty_level(int(game_mode_choice))
                case "0":
                    game_on = False
                case _:
                    print ("Invalid choice. Try again.")
                    game_on = True
        return False

    def select_difficulty_level(self, no_of_players:int) -> bool:
        difficulty_level_menu = """
        Select Difficulty Level:
        1. Easy (3 X 3)
        2. Hard (4 X 4)
        3. Extreme (3 X 3 X 3)
        4. Dangerous (4 X 4 X 4)
        0. |<- go back.
        """

        game_on = True
        while game_on:
            difficulty_level_choice = input(difficulty_level_menu)
            match difficulty_level_choice:
                case "1":
                    game_on = self.start_game(no_of_players, int(difficulty_level_choice))
                case "2":
                    game_on = self.start_game(no_of_players, int(difficulty_level_choice))
                case "3":
                    game_on = self.start_game(no_of_players, int(difficulty_level_choice))
                case "4":
                    game_on = self.start_game(no_of_players, int(difficulty_level_choice))
                case "0":
                    game_on = self.select_game_mode()
                case _:
                    print ("Invalid choice. Try again.")
                    game_on = True
        return False

    @staticmethod
    def start_game(no_of_players:int, difficulty_level:int):
        tic_tac_toe = TicTacToeGame(no_of_players, difficulty_level)
        print("""
                +-----------------------+
                |   Tic-Tac-Toe Game    |
                |       GAME ON!!       |
                +-----------------------+
        """)
        tic_tac_toe.start_game()

Main().main()
