from bankservice.bank import Bank


class OkoliBankAtm:
    bank: Bank = None
    BANK_NAME = "Okoli Bank Plc Nigeria"

    def main(self):
        self.bank = Bank(self.BANK_NAME)
        self.main_menu(success_message("WELCOME TO OUR BANK"))


    def clear_screen(self):
        pass


    def main_menu(self, prompt:str) -> None:
        self.clear_screen()
        menu_prompt = self.BANK_NAME + """
        
        Main Menu:
        1: Create Account
        2: Deposit
        3: Withdraw
        4: Transfer
        5: Check Balance
        6: Account Settings
        0: Exit
        
        """ + prompt + "\n>>>"

        choice: int = self.input_integer(menu_prompt)
        match choice:
            case 1: self.create_account()
            case 2: self.deposit()
            case 3: self.withdraw()
            case 4: self.transfer()
            case 5: self.check_balance()
            case 6: self.account_settings()
            case 0: self.exit_bank()
            case _: self.main_menu(self.error_message("Invalid selection: Try again"))

    def create_account(self) -> None:
        first_name = self.input_text("Enter your first name: ")
        last_name = self.input_text("Enter your last name: ")
        pin = self.input_text("Enter your PIN code ")
        account_number:str
        try:
            account_number = self.bank.create_account(first_name, last_name, pin)
            self.main_menu(self.success_message("Account Created Successfully!\n") + self.info_message(self.account_info(account_number)))
        except ValueError as e:
            self.main_menu(self.error_message(e))

    def deposit(self) -> None:
        account_number = self.input_integer("Enter your account number: ")
        amount = self.input_integer("Enter your deposit amount: ")
        try:
            self.bank.deposit(account_number, amount)
            self.main_menu(self.successMessage(self.format_amount_output(amount) + " Deposit Successful!\n"))
        except ValueError as e:
            self.main_menu(self.error_message("Deposit Failed!: " + str(e)))

    def withdraw(self) -> None:
        account_number = self.input_integer("Enter your account number: ")
        amount = self.input_integer("Enter your withdrawal amount: ")
        pin = self.input_integer("Enter your PIN code: ")
        try:
            self.bank.withdraw(account_number, amount, pin)
            self.main_menu(self.success_message(self.format_amount_output(amount) + " Withdraw Successful!\n"))
        except ValueError as e:
            self.main_menu(self.error_message("Withdraw Failed!: " + str(e)))

    def transfer(self) -> None:
        source_account_number = self.input_integer("Enter your source account number: ")
        destination_account_number = self.input_integer("Enter your destination account number: ")
        amount = self.input_integer("Enter your transfer amount: ")
        try:
            transfer_prompt = ("Transfer {} to {} ({})\nTo proceed, please enter your PIN code: "
                               .format(self.format_amount_output(amount), destination_account_number,
                                       self.get_full_name(destination_account_number)))
            pin = self.input_text(self.info_message(transfer_prompt))
            self.bank.transfer(source_account_number, destination_account_number, amount, pin)
            self.main_menu(self.success_message(self.format_amount_output(amount) + " Transfer Successful!\n"))
        except ValueError as e:
            self.main_menu(self.error_message("Transfer Failed:" + str(e)))

    def check_balance(self) -> None:
        account_number = self.input_integer("Enter your account number: ")
        pin = self.input_text("Enter your PIN code: ")
        try:
            balance = self.bank.check_balance(account_number, pin)
            self.main_menu(self.info_message(f"Your balance is {self.format_amount_output(balance)}!\n"))





