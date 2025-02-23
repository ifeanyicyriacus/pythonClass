from src.diary_services.diary import Diary
from src.diary_services.entry import Entry

from src.main_application.main_menu import MainMenu
from src.main_application.diary_settings_menu import DiarySettingsMenu

class DiaryMenu:
    incorrect_input = 3

    @classmethod
    def diary_menu(cls, notification:str, diary: Diary):
        diary_menu_prompt = """
        
        -----ONWARD DIARY SERVICE------
                Diary Menu:
                1 -> Add new Entry
                2 -> View your Entries (""" + diary.number_of_entries + """
                )
                3 -> Update Entry
                4 -> Find Entry
                5 -> Delete Entry
                """ + "6 -> {} diary".format("Unlock" if diary.is_locked else "Lock") + """
                7 -> Change Diary Settings
                8 -> Log Out
                0 -> Exit
                
        """ + notification + "\n>>>"

        choice = MainMenu.input_number(diary_menu_prompt)
        match choice:
            case 1: cls.add_entry(diary)
            case 2: cls.read_entries(diary)
            case 3: cls.update_entry(diary)
            case 4: cls.find_entry(diary)
            case 5: cls.delete_entry(diary)
            case 6: cls.toggle_diary_lock(diary)
            case 7: DiarySettingsMenu.diary_settings_menu(MainMenu.info_message("Remember to take note of your new changes"), diary)
            case 8: cls.log_out(diary)
            case 9: MainMenu.exit_diary()
            case _:
                count = cls.incorrect_input
                if cls.incorrect_input == 0:
                    cls.incorrect_input = 3
                    MainMenu.exit_diary()
                    cls.incorrect_input -= 1
                cls.diary_menu(MainMenu.error_message(f"Invalid selection, try again. ({count} tries left)"), diary)

    @classmethod
    def add_entry(cls, diary) -> None:
        MainMenu.clear_screen()
        if diary.is_locked():
            print(MainMenu.info_message("Diary is locked"))
            cls.toggle_diary_lock(diary)
        print("Adding new Entries...")
        title = MainMenu.input_str("Please enter title: ")
        body = MainMenu.input_str("Please enter body: ")
        try:
            diary.create_entry(title, body)
        except ValueError as e:
            cls.diary_menu(MainMenu.error_message(str(e)), diary)
        cls.diary_menu(MainMenu.success_message(f"({title}) added successfully"), diary)

    @classmethod
    def read_entries(cls, diary) -> None:
        cls.diary_menu(str(diary), diary)

    @classmethod
    def get_entry(cls, diary) -> Entry:
        MainMenu.clear_screen()
        entry_id = MainMenu.input_number("Please enter entry ID: ")
        try:
            return diary.find_entry_by_id(entry_id)
        except ValueError as e:
            cls.diary_menu(MainMenu.error_message(str(e)), diary)
        MainMenu.clear_screen()

    @classmethod
    def update_entry(cls, diary:Diary) -> None:
        entry:Entry = cls.get_entry(diary)
        is_confirmed = cls.get_confirmation("Are you sure you want to update this entry (y/n)?", entry)
        if is_confirmed and entry is not None:
            new_title = MainMenu.input_str("Please enter a new title (or enter to skip): ")
            new_body = MainMenu.input_str("Please enter a new body (or enter to skip): ")
            new_title = entry.title if new_title is None else new_title
            new_body = entry.body if new_body is None else new_body
            diary.update_entry(entry.entry_id, new_title, new_body)
            cls.diary_menu(MainMenu.success_message("Update was successful!"), diary)
        else:
            cls.diary_menu(MainMenu.info_message("No changes were made!"), diary)

    @classmethod
    def find_entry(cls, diary: Diary) -> None:
        entry:Entry = cls.get_entry(diary)
        if entry is not None:
            cls.diary_menu(str(entry), diary)

    @classmethod
    def delete_entry(cls, diary: Diary) -> None:
        entry:Entry = cls.get_entry(diary)
        is_confirmed:bool = cls.get_confirmation("Are you sure you want to delete this entry (y/n)?", entry)
        if is_confirmed and entry is not None:
            diary.delete(entry.entry_id)
            cls.diary_menu(MainMenu.success_message("Successfully deleted the entry"), diary)
        else:
            cls.diary_menu(MainMenu.info_message("Deletion was avoided - phew! close call!"), diary)

    @classmethod
    def get_confirmation(cls, prompt: str, entry:Entry) -> bool:
        confirmation_prompt:str = f"{entry}\n{prompt}"
        return MainMenu.get_confirmation(confirmation_prompt)

    @classmethod
    def toggle_diary_lock(cls, diary: Diary) -> None:
        if not diary.is_locked():
            diary.lock()
            cls.diary_menu(MainMenu.info_message("Mischief managed🪄 : Diary is locked! "), diary)
        else:
            password = MainMenu.input_str("Please enter your password to unlock: ")
            try:
                diary.unlock(password)
                cls.diary_menu(MainMenu.success_message("Diary unlocked!"), diary)
            except ValueError as e:
                cls.diary_menu(MainMenu.error_message(str(e)), diary)

    @classmethod
    def log_out(cls, diary: Diary) -> None:
        diary.lock()
        MainMenu.main_menu(MainMenu.success_message("Log out!!!"))

