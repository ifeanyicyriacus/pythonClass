def even_adder(list_of_numbers : list):
    sum = 0
    for number in list_of_numbers:
        if number % 2 == 0:
            sum += number
    return sum
    
    
def vowel_counter(text : str) -> int:
    sum = 0
    vowels = ["a", "e", "i", "o", "u"]
    text = text.lower()
    for letter in text:
        if letter in vowels:
            sum += 1
    return sum

def anagram_checker(text1 : str, text2 : str) -> bool:
    text1 = text1.lower()
    text2 = text2.lower()
    if len(text1) != len(text2):
        return False
    else:
        for letter in text1:
            text1 = text1.replace(letter, "")
            text2 = text2.replace(letter, "")
            if len(text1) != len(text2):
                return False
        else:
            return True
    
def prime_checker(number : int) -> bool:
    for value in range(2, number):
        if number % value == 0:
            return False
    return True
    
def string_palindrome_checker(word : str) -> bool:
    word = word.lower()
    if word == word[::-1]:
        return True
    return False
        
def reverse_string(text : str) -> str:
    return text[::-1]
    
def get_average(number_list : list) -> float:
    sum = 0.0
    for number in number_list:
        sum += number
    return sum/len(number_list)

def capitalise_list(word_list : list) -> list:
    for index in range(len(word_list)):
        word_list[index] = word_list[index].capitalize()
    return word_list
    
def duplicate_checker(number_list: list) -> bool:
    for index_a in range(len(number_list) - 1):
        for index_b in range((index_a + 1), len(number_list)):
            if number_list[index_a] == number_list[index_b]:
                return True
    return False

def white_space_remover(text : str) -> str:
    return text.replace(" ", "")

def get_list_intercept(list1:list, list2:list) -> str:
    result = []
    for element in list1:
        if element in list2 and element not in result:
            result.append(element)
    return result


def sum_of_product(int_list : list) -> int:
    total  = 0
    product = 0
    for index in range(len(int_list) - 1):
        product += (int_list[index] * int_list[index + 1])
    for index in int_list:
        total += index
    return total + product

def sort_word_list_by_length(word_list : list) -> list:
    for counter1 in range(len(word_list)):
        for counter2 in range(counter1, len(word_list)):
            if len(word_list[counter1]) > len(word_list[counter2]):
                temp = word_list[counter2]
                word_list[counter2] = word_list[counter1]
                word_list[counter1] = temp
                counter2 = 0
    return word_list

def number_factorial(number:int) -> int:
    product = 1
    for number in range(1, (number+1)):
        product *= number
    return product

def sum_of_number_digit(number : int) -> int:
    return sum([int(x) for x in str(number)])

def sum_of_number_odd_digit(number : int) -> int:
    return sum([int(x) if (int(x) % 2 != 0) else 0 for x in str(number)])

def merge_and_sort(int_list_a : list, int_list_b : list) -> list:
    return sorted(int_list_a + int_list_b)

def acronym(text : str) -> str:
    result = ""
    for word in text.split():
        result += word[0].upper()
    return result
    
    
    
    
#extra task
def ignore_index(int_list : list) -> int:
    total = 0
    for indexA in range(len(int_list)):
        for indexB in range(len(int_list)):
            if indexA == indexB:
                continue
            total += int_list[indexB]
    return total

def ignore_index_method_2(int_list : list) -> int:
    result = sum([x for x in int_list]) * (len(int_list) - 1)
    return result
    


    
