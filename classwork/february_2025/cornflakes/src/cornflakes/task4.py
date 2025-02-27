def sort_text_by_case(test:str):
    result = ["", ""]
    for char in test:
        if char.isupper():
            result[0] += char
        elif char.islower():
            result[1] += char
    return result[0] + result[1]
