import sys

from src.seven_segment_display.seven_segment_display import SevenSegmentDisplay


class Main:
    display:SevenSegmentDisplay = SevenSegmentDisplay()

    menu_prompt = """
    ------SEVEN SEGMENT DISPLAY----
    1. Prompt Segment Display (8-digit binary)
    0. Exit
    
    """
    @staticmethod
    def start():
        while True:
            user_input:str = input(Main.menu_prompt)
            if user_input == "0": sys.exit(0)
            elif user_input == "1":
                user_input = input("Enter 8-digit binary to continue...:")
                try:
                    Main.display.enter_prompt(user_input)
                    print(Main.display)
                except ValueError as e:
                    print(str(e))
            else:
                print(f"Invalid Selection ({user_input}): Please enter either 1 or O")

Main().start()
