import sys
from bankservice.bank import Bank
# from account_settings_menu import account_settings_menu

BANK_NAME = "Okoli Bank Plc Nigeria"
bank:Bank = Bank(BANK_NAME)

def exit_bank() -> None:
    sys.exit(0)

def clear_screen() -> None:
    print("\033[H\033[2J")

def format_amount_output(amount:int) -> str:
    amount = list(str(amount))

    result = ""
    i = len(amount) - 1
    count = 1
    while i >= 0:
        result = amount[i] + result
        result = "{}{}".format(amount[i], result)
        if count % 3 == 0:
            result = "{}{}".format(",", result)
        i -= 1
        count = count + 1
    return f"{'₦ '}{result}"

def error_message(message:str) -> str:
    return "\033[31m" + message + "\033[0m"

def success_message(message:str) -> str:
    return "\033[32m" + message + "\033[0m"

def info_message(message:str) -> str:
    return "\033[33m" + message + "\033[0m"

def input_integer(prompt:str) -> int:
    try:
        value = input(prompt)
        # value = value.replace(r"\\s", "").replace(r"[_,]", "")
        return int(value)
    except ValueError as e:
        print(error_message("Value should be an integer, only (',' and '_') are acceptable separator"))
        return input_integer(prompt)

def input_text(prompt:str) -> str:
    value = input(prompt)
    if value == "":
        print(error_message("Your input is empty! Try Again."))
        return input_text(prompt)
    else: return value

def main():
    main_menu(success_message("WELCOME TO OUR BANK"))

def main_menu(prompt:str) -> None:
    clear_screen()
    menu_prompt = BANK_NAME + """
    
    Main Menu:
    1: Create Account
    2: Deposit
    3: Withdraw
    4: Transfer
    5: Check Balance
    6: Account Settings
    0: Exit
    
    """ + prompt + "\n>>>"

    choice: int = input_integer(menu_prompt)
    match choice:
        case 1: create_account()
        case 2: deposit()
        case 3: withdraw()
        case 4: transfer()
        case 5: check_balance()
        case 6: account_settings()
        case 0: exit_bank()
        case _: main_menu(error_message("Invalid selection: Try again"))

def create_account() -> None:
    first_name = input_text("Enter your first name: ")
    last_name = input_text("Enter your last name: ")
    pin = input_text("Enter your PIN code ")
    account_number:str
    try:
        account_number = bank.create_account(first_name, last_name, pin)
        main_menu(
            success_message("Account Created Successfully!\n") + info_message(account_info(account_number)))
    except ValueError as e:
        main_menu(error_message(e))

def deposit() -> None:
    account_number = input_integer("Enter your account number: ")
    amount = input_integer("Enter your deposit amount: ")
    try:
        bank.deposit(account_number, amount)
        main_menu(success_message(format_amount_output(amount) + " Deposit Successful!\n"))
    except ValueError as e:
        main_menu(error_message("Deposit Failed!: " + str(e)))

def withdraw() -> None:
    account_number = input_integer("Enter your account number: ")
    amount = input_integer("Enter your withdrawal amount: ")
    pin = input_integer("Enter your PIN code: ")
    try:
        bank.withdraw(account_number, amount, pin)
        main_menu(success_message(format_amount_output(amount) + " Withdraw Successful!\n"))
    except ValueError as e:
        main_menu(error_message("Withdraw Failed!: " + str(e)))

def transfer() -> None:
    source_account_number = input_integer("Enter your source account number: ")
    destination_account_number = input_integer("Enter your destination account number: ")
    amount = input_integer("Enter your transfer amount: ")
    try:
        transfer_prompt = ("Transfer {} to {} ({})\nTo proceed, please enter your PIN code: "
                           .format(format_amount_output(amount), destination_account_number,
                                   get_full_name(str(destination_account_number))))
        pin = input_text(info_message(transfer_prompt))
        bank.transfer(source_account_number, destination_account_number, amount, pin)
        main_menu(success_message(format_amount_output(amount) + " Transfer Successful!\n"))
    except ValueError as e:
        main_menu(error_message("Transfer Failed:" + str(e)))

def check_balance() -> None:
    account_number = input_integer("Enter your account number: ")
    pin = input_text("Enter your PIN code: ")
    try:
        balance = bank.check_balance(account_number, pin)
        main_menu(info_message(f"Your balance is {format_amount_output(balance)}!\n"))
    except ValueError as e:
        main_menu(error_message("Check Balance Failed!: " + str(e)))

def account_settings() -> None:
    account_number = input_integer("Enter your account number: ")
    greetings = "Hello " + get_full_name(str(account_number))
    account_settings_menu(greetings, account_number)

def account_info( account_number:str) -> str:
    full_name = get_full_name(account_number)
    return ("{}\nAccount number: {}\nAccount name: {}\n{}\n"
            .format("-"*10, account_number, full_name, "-"*10))

def get_full_name( account_number:str) -> str:
    try:
        return (bank.get_account_first_name(account_number) + " "
                + bank.get_account_last_name(account_number))
    except ValueError as e:
        main_menu(error_message(str(e)))

# ######

def account_settings_menu(prompt: str, account_number: int) -> None:
    clear_screen()
    menu_prompt = BANK_NAME + """

    Main Menu/Update Profile:
    1: Change First Name
    2: Change Last Name
    3: Reset PIN
    4: |<- Go back to Main Menu
    0: Exit
    """ + prompt + "\n>>>"

    choice = input_integer(menu_prompt)
    match choice:
        case 1:
            update_first_name(account_number)
        case 2:
            update_last_name(account_number)
        case 3:
            reset_pin(account_number)
        case 4:
            main_menu((success_message("Welcome again!!!")))
        case 0:
            exit_bank()
        case _:
            account_settings_menu(error_message("Invalid selection: Try again"), account_number)


def update_first_name(account_number: int) -> None:
    new_first_name = input_text("Enter new first name: ")
    pin = input_text("Enter new pin: ")
    try:
        bank.update_first_name(account_number, new_first_name, pin)
        account_settings_menu(success_message("First name set to: " + new_first_name), account_number)
    except Exception as e:
        account_settings_menu(error_message("Update failed: " + str(e)), account_number)


def update_last_name(account_number: int) -> None:
    new_last_name = input_text("Enter new last name: ")
    pin = input_text("Enter new pin: ")
    try:
        bank.update_last_name(account_number, new_last_name, pin)
        account_settings_menu(success_message("Last name set to: " + new_last_name), account_number)
    except Exception as e:
        account_settings_menu(error_message("Update failed: " + str(e)), account_number)


def reset_pin(account_number: int) -> None:
    current_pin = input_text("Enter new PIN: ")
    new_pin = input_text("Enter your new PIN: ")
    try:
        bank.reset_pin(account_number, current_pin, new_pin)
        account_settings_menu(success_message("Reset PIN to: " + new_pin), account_number)
    except Exception as e:
        account_settings_menu(error_message("Reset PIN failed: " + str(e)), account_number)



# ######
main()


