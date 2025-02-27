from src.cornflakes.task1 import character_frequency_calculator as cfc

def find_letter_frequency(word:str, keyword:str) -> tuple:
    letters_dict:dict = cfc(word)
    return keyword, letters_dict[keyword]