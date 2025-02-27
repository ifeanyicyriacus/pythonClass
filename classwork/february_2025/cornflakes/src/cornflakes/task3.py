def add_character_to_middle_or_end(text:str, character:str) -> str:
    if len(text) % 2 == 0:
        return text[0:(len(text)//2)] + character + text[len(text)//2:]
    else:
        return text + character