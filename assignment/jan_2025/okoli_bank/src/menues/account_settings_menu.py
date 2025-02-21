from menues.okoli_bank_atm import BANK_NAME, clear_screen, input_integer, success_message, main_menu, exit_bank, \
    error_message, input_text, bank
#
# def account_settings_menu(prompt:str, account_number:int) -> None:
#     clear_screen()
#     menu_prompt = BANK_NAME + """
#
#     Main Menu/Update Profile:
#     1: Change First Name
#     2: Change Last Name
#     3: Reset PIN
#     4: |<- Go back to Main Menu
#     0: Exit
#     """ + prompt + "\n>>>"
#
#     choice = input_integer(menu_prompt)
#     match choice:
#         case 1: update_first_name(account_number)
#         case 2: update_last_name(account_number)
#         case 3: reset_pin(account_number)
#         case 4: main_menu((success_message("Welcome again!!!")))
#         case 0: exit_bank()
#         case _: account_settings_menu(error_message("Invalid selection: Try again"), account_number)
#
# def update_first_name(account_number:int) -> None:
#     new_first_name = input_text("Enter new first name: ")
#     pin = input_text("Enter new pin: ")
#     try:
#         bank.update_first_name(account_number, new_first_name, pin)
#         account_settings_menu(success_message("First name set to: " + new_first_name), account_number)
#     except Exception as e:
#         account_settings_menu(error_message("Update failed: " + str(e)), account_number)
#
# def update_last_name(account_number:int) -> None:
#     new_last_name = input_text("Enter new last name: ")
#     pin = input_text("Enter new pin: ")
#     try:
#         bank.update_last_name(account_number, new_last_name, pin)
#         account_settings_menu(success_message("Last name set to: " + new_last_name), account_number)
#     except Exception as e:
#         account_settings_menu(error_message("Update failed: " + str(e)), account_number)
#
# def reset_pin(account_number:int) -> None:
#     current_pin = input_text("Enter new PIN: ")
#     new_pin = input_text("Enter your new PIN: ")
#     try:
#         bank.reset_pin(account_number, current_pin, new_pin)
#         account_settings_menu(success_message("Reset PIN to: " + new_pin), account_number)
#     except Exception as e:
#         account_settings_menu(error_message("Reset PIN failed: " + str(e)), account_number)