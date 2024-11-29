def multiply_by_two(numbers:list) -> list:
    #return [x*2 for x in numbers]
    return list(map(lambda x: x*2, numbers))
    
def find_by_length(texts:list, length:int) -> list:
    #return [text for text in texts if len(text) >= length]
    return list(filter(lambda text: len(text) >= length, texts))
    
def digit_adder(number:int) -> int:
    #return sum([int(x) for x in str(number)])
    #return sum(list(map(int, str(number))))
    return sum(list(map (lambda num: int(num), str(number))))

def remove_all_vowels(words:list) -> list:
    #return [word_to_non_vowel(x) for x in words]
    return list(map(word_to_non_vowel,  words))

def word_to_non_vowel(word:str) -> str:
    vowel = "AEIOU"
    result = ""
    for char in word:
        if char.upper() not in vowel:
            result += char
    return result

def dict_generator() -> dict:
    return {x : x**2 for x in range(1, 11) if x % 2 == 0}
    
def lists_to_dict(list1:list, list2:list) -> dict:
    return {x:y for x,y in zip(list1, list2)}
    
def dictionary_to_value_list(dict1:dict) -> list:
    return [x for x in dict1.values()]
    
def update_and_add_to_dict(dict1:dict, dict2:dict) -> dict:
    for key, value in dict2.items():
        dict1[key] = value
    return dict1

def key_value_swapping(dict1:dict) -> dict:
    return {y:x for x, y in dict1.items()}


