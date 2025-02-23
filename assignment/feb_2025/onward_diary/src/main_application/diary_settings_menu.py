from diary_services.diary import Diary
from main_application.diary_menu import DiaryMenu
from src.main_application.main_menu import MainMenu


class DiarySettingsMenu:

    @staticmethod
    def diary_settings_menu(notification:str, diary:Diary):
        MainMenu.clear_screen()
        diary_settings_menu_prompt = """
        -----ONWARD DIARY SERVICE------
        Diary Settings:
        1 -> Change Diary username
        2 -> Change Diary password
        3 -> Go Back
        0 -> Exit
                
        """ + notification + "\n>>>"
        choice = MainMenu.input_number(diary_settings_menu_prompt)
        match choice:
            case 1: DiarySettingsMenu.change_diary_username(diary)
            case 2: DiarySettingsMenu.change_diary_password(diary)
            case 3: DiaryMenu.diary_menu(MainMenu.info_message("Welcome to your diary."), diary)
            case 0: MainMenu.exit_diary()
            case _: DiarySettingsMenu.diary_settings_menu(MainMenu.error_message("Invalid selection, Try again."), diary)
        DiaryMenu.diary_menu(MainMenu.success_message("Your changes were successful"), diary)

    @staticmethod
    def change_diary_username(diary:Diary) -> None:
        if diary.is_locked:
            DiaryMenu.toggle_diary_lock(diary)

        old_username = diary.username
        confirmation_prompt = "Your old username is ({})\n"
        "Are you sure you want to change your username (y/n)?".format(old_username)
        is_confirmed:bool = MainMenu.get_confirmation(confirmation_prompt)

        if is_confirmed:
            new_username = MainMenu.input_str("Please enter your new username: ")
            password = MainMenu.input_str("Please enter your password to authorise your changes: ")
            try:
                diary.change_username(new_username, password)
                DiarySettingsMenu.diary_settings_menu(MainMenu.success_message(
                    "Your username was changed successfully."))
            except ValueError as e:
                DiarySettingsMenu.diary_settings_menu(MainMenu.error_message(str(e)), diary)
        else: DiarySettingsMenu.diary_settings_menu(MainMenu.info_message("No changes were made."), diary)

    @staticmethod
    def change_diary_password(diary:Diary) -> None:
        if diary.is_locked:
            DiaryMenu.toggle_diary_lock(diary)

        confirmation_prompt = "Are you sure you want to change your password (y/n)?"
        is_confirmed:bool = MainMenu.get_confirmation(confirmation_prompt)

        if is_confirmed:
            new_password:str = MainMenu.input_str("Please enter your new password: ")
            current_password = MainMenu.input_str("Please enter your current password to authorise change: ")
            try:
                diary.change_password(new_password, current_password)
                DiarySettingsMenu.diary_settings_menu(MainMenu.success_message(
                    "Your password was changed successfully."), diary)
            except ValueError as e:
                DiarySettingsMenu.diary_settings_menu(MainMenu.error_message(str(e)), diary)
        else:
            DiarySettingsMenu.diary_settings_menu(MainMenu.info_message("No changes were made."), diary)
