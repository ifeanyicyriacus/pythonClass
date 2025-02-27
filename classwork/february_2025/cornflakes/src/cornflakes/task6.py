from string import punctuation

def remove_special_characters(word: str) -> str:
    result = ""
    for char in word:
        if char not in punctuation:
            result += char
    return result
