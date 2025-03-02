import string

class SevenSegmentDisplay:

    def __init__(self):
        self.display = [
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "]
        ]

    token = "#"

    def enter_prompt(self, prompt:str):
        for char in prompt:
            if char in string.printable[10:]:
                raise ValueError("Only numbers are allowed")
            if char in string.digits[2:]:
                raise ValueError("Only zero(0) and one(1) are allowed")
            if len(prompt) != 8:
                raise ValueError("Length of input should be exactly 8 characters long")
        self.set_segments_value(prompt)

    def set_segments_value(self, prompt:str):
        prompt_char = [x for x in prompt]
        self.__set_display_blank()
        if prompt_char[7] == "1":
            self.__set_a(prompt_char[0] == "1")
            self.__set_b(prompt_char[1] == "1")
            self.__set_c(prompt_char[2] == "1")
            self.__set_d(prompt_char[3] == "1")
            self.__set_e(prompt_char[4] == "1")
            self.__set_f(prompt_char[5] == "1")
            self.__set_g(prompt_char[6] == "1")


    def __set_a(self, state:bool) -> None:
        index = 0
        while state and index < 4:
            self.display[0][index] =  self.token
            index += 1

    def __set_b(self, state:bool) -> None:
        index = 0
        while state and index < 3:
            self.display[index][3] = self.token
            index += 1

    def __set_c(self, state:bool) -> None:
        index = 2
        while state and index < 5:
            self.display[index][3] = self.token
            index += 1

    def __set_d(self, state:bool) -> None:
        index = 3
        while state and index >= 0:
            self.display[4][index] = self.token
            index -= 1

    def __set_e(self, state:bool) -> None:
        index = 4
        while state and index >= 2:
            self.display[index][0] = self.token
            index -= 1

    def __set_f(self, state:bool) -> None:
        index = 2
        while state and index >= 0:
            self.display[index][0] = self.token
            index -= 1

    def __set_g(self, state:bool) -> None:
        index = 0
        while state and index < 4:
            self.display[2][index] = self.token
            index += 1

    def __toggle_display_on_or_off(self, state:bool) -> None:
        if not state: self.__set_display_blank()

    def __set_display_blank(self):
        index = 0
        while index < len(self.display):
            self.display[index] = [" ", " ", " ", " "]
            index += 1

    def get_display(self) -> [[]]:
        return self.display

    def __str__(self) -> str:
        result = ""
        for row in self.display:
            for char in row:
                result += char
            result += "\n"
        return result



