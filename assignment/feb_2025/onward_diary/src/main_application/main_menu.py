import sys

from src.diary_services.diaries import Diaries
from src.diary_services.diary import Diary

from src.main_application.diary_menu import DiaryMenu

class MainMenu:
    diaries: Diaries = Diaries()

    @classmethod
    def main(cls):
        try:
            cls.main_menu(cls.success_message("Welcome!!!"))
        except Exception as e:
            cls.main_menu(cls.error_message(str(e)))

    @classmethod
    def main_menu(cls, notification):
        cls.clear_screen()
        main_menu_prompt:str = """
        -----ONWARD DIARY SERVICE------
        Main Menu:
        1 -> Add Diary
        2 -> Open Diary
        3 -> Delete Diary
        0 -> Exit
        
        """ + notification + "\n>>>"

        choice = cls.input_number(main_menu_prompt)
        match choice:
            case 1: cls.add_diary()
            case 2: cls.open_diary()
            case 3: cls.delete_diary()
            case 0: cls.exit_diary()
            case _: cls.main_menu(cls.error_message("Invalid selection, Try again."))

    @classmethod
    def add_diary(cls):
        username:str = cls.input_str("Enter your username: ")
        password:str = cls.input_str("Enter your password: ")

        try:
            cls.diaries.add(username, password)
        except Exception as e:
            cls.print(str(e))
            cls.add_diary()
        cls.main_menu(cls.success_message("New diary added successfully for user: " + username))

    @classmethod
    def get_diary(cls, username:str) -> Diary:
        try:
            diary = cls.diaries.find_by_username(username)
            return diary
        except Exception as e:
            cls.main_menu(cls.error_message(str(e)))

    @classmethod
    def open_diary(cls) -> None:
        username:str = cls.input_str("Please enter your username: ")
        diary:Diary = cls.get_diary(username)
        DiaryMenu.diary_menu(cls.success_message(username + ", Welcome to your diary."), diary)

    @classmethod
    def delete_diary(cls) -> None:
        username:str = cls.input_str("Please enter your username: ")
        password:str = cls.input_str("Enter your password: ")
        no_of_entries:int = cls.get_diary(username).number_of_entries

        confirmation_prompt:str = ("Your diary has {} entris.\nAre you sure you want to delete this diary? (y/n)"
                                   .format(no_of_entries))
        is_confirmed:bool = cls.get_confirmation(confirmation_prompt)

        if is_confirmed:
            try:
                cls.diaries.delete(username, password)
                cls.main_menu(cls.success_message("Successfully deleted diary."))
            except Exception as e:
                cls.main_menu(cls.error_message(str(e)))
        else:
            cls.main_menu(cls.info_message("Deletion attempt was avoided - close call!"))

    @staticmethod
    def exit_diary():
        sys.exit(0)

    @classmethod
    def get_confirmation(cls, confirmation_prompt:str) -> bool:
        choice = cls.input_str(cls.info_message(confirmation_prompt))
        match choice.lower():
            case "y": return True
            case "n": return False
            case _:
                cls.print("Invalid selection, only 'Y' and 'N' are valid, try again.")
                cls.get_confirmation(confirmation_prompt)

    @classmethod
    def input_str(cls, prompt:str) -> str:
        try:
            value = input(prompt)
            if value == "": raise ValueError("Field cannot be blank")
            else: return value
        except ValueError as e:
            cls.clear_screen()
            cls.print(cls.error_message(str(e)))
            return cls.input_str(prompt)

    @classmethod
    def input_number(cls, prompt:str) -> int:
        try:
            return int(cls.input_str(prompt))
        except ValueError as e:
            cls.clear_screen()
            cls.print(cls.error_message("Only numbers are allowed. Try again."))
            return cls.input_number(prompt)

    @staticmethod
    def print(prompt:str):
        print(prompt)

    @classmethod
    def clear_screen(cls):
        cls.print("\033c")
        # cls.print("\033[H\033[2J")

    @staticmethod
    def error_message(text:str) -> str:
        return f"\033[31m{text}\033[0m"

    @staticmethod
    def success_message(text:str) -> str:
        return f"\033[32m{text}\033[0m"

    @staticmethod
    def info_message(text:str) -> str:
        return f"\033[33m{text}\033[0m"


MainMenu.main()