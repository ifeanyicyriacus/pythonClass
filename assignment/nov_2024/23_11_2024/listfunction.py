def find_largest_from(numbers:list) -> int:
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

def reverse_list(numbers:list) -> list:
    return numbers[::-1]

def check_if_exist(numbers:list, number:int) -> bool:
    for element in numbers:
        if number == element:
            return True
    return False

def return_odd_position_element(numbers:list) -> list:
    odd_number_list = []
    toggle = True
    for number in numbers:
        if toggle:
            odd_number_list.append(number)
        toggle = not toggle
    return odd_number_list

def return_even_position_element(numbers:list) -> list:
    even_number_list = []
    toggle = False
    for number in numbers:
        if toggle:
            even_number_list.append(number)
        toggle = not toggle
    return even_number_list
    
def get_running_total(numbers:list) -> list:
    total = 0
    for number in numbers:
        total += number
    return total

def check_if_palindrome(text:str) -> bool:
    text = text.upper()
    return text == text[::-1]
    
def sum_using_for_loop(numbers:list) -> int:
    sum = 0
    for number in numbers:
        sum += number
    return sum

def sum_using_while_loop(numbers:list) -> int:
    sum = 0
    count = 0
    while count< len(numbers):
        sum += numbers[count]
        count += 1
    return sum

def concatinate_lists(list_1:list, list_2:list) -> list:
    return list_1 + list_2
    
def alternating_concatination(list_1:list, list_2:list) -> list:
    length_1 = len(list_1)
    length_2 = len(list_2)
    total_length = length_1 + length_2
    
    new_list = []
    max_length = length_1 if (length_1 >= length_2) else length_2
    
    for index in range(max_length):
        if index < length_1:
            new_list.append(list_1[index])
        if index < length_2:
            new_list.append(list_2[index])
    return new_list

def number_to_list_of_digit(number:int) -> list:
    length = len(str(number))
    crop_a = 10; crop_b = 1;
    count = 0
    digits = []
    while count < length:
        digit = (number % crop_a) // crop_b
        digits.insert(0, digit)
        crop_a *= 10; crop_b *= 10;
        count += 1
    return digits
