import random

def generate_password() -> str:
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = lower_alphabet.upper()
    numbers = "0123456789"
    symbols = "`~!@#$%^&*()_-+=\\|}][{'\":;/?>.,<"

    character_groups = [lower_alphabet, upper_alphabet, numbers, symbols]
    sample = "".join(character_groups)
    
    password_list = []
    is_not_secure = True
    while (is_not_secure):
        password_list = random.choices(sample, k = 16)
        
        if allCharacterTypeAreRepresentedIn(password_list, character_groups):
            is_not_secure = False
        else:
            continue

    return "".join(password_list)
    
def allCharacterTypeAreRepresentedIn(password_list:list, character_groups:list) -> bool:
    for character_group in character_groups:
        if all([character not in character_group for character in password_list]):
            return False
    return True

