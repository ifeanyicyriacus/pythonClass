import string


def shift_alphabet(letter, shift) -> str:
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase

    if letter.islower():
        letter_index = lowercase.index(letter)
        encrypted_index = (letter_index + shift) % 26
        return lowercase[encrypted_index]
    else:
        letter_index = uppercase.index(letter)
        encrypted_index = (letter_index + shift) % 26
        return uppercase[encrypted_index]


def encrypt_text(text:str) -> str:
    result = ""
    for letter in text:
        if letter.isalpha():
            result += shift_alphabet(letter, 13)
        else:
            result += letter
    return result

# def decrypt_text(text:str) -> str:
#     result = ""
#     for letter in text:
#         if letter.isalpha():
#             result += shift_alphabet(letter, (26 - 13))
#         else:
#             result += letter
#     return result