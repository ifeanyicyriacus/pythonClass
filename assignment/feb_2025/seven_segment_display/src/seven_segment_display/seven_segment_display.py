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
        self.set_segments_value(prompt)

    def set_segments_value(self, prompt:str):
        prompt_char = [x for x in prompt]
        self.__set_display_blank()
        self.__set_a(prompt_char[0] == "1")
        self.__set_a(prompt_char[1] == "1")
        self.__set_a(prompt_char[2] == "1")
        self.__set_a(prompt_char[3] == "1")
        self.__set_a(prompt_char[4] == "1")
        self.__set_a(prompt_char[5] == "1")
        self.__set_a(prompt_char[6] == "1")
        self.__toggle_display_on_or_off(prompt_char[7] == "1")


    def __setA(self, state:bool):
        index = 0
        while index < 4:
            self.display[0][index] =  self.token if state else self.display[0][index]

