def get_switched_list(int_list:list, count:int) -> list:
    for _ in range(count):
        head = int_list.pop(0)
        int_list.append(head)
    return int_list
    
def split_in_half(int_list:list) -> list:
    new_list = []
    length = len(int_list)
    even = True if (length % 2 == 0) else False
    middle = length // 2
    if even:
        new_list.append(int_list[:middle])
        new_list.append(int_list[middle:])
    else:
        new_list.append(int_list[ : (middle + 1)])
        new_list.append(int_list[(middle + 1) : ])
    return new_list

def check_if_list_are_even(int_list:list) -> list:
    boolean_list = []
    index = 0
    for number in int_list:
        boolean_list.append(True if (number % 2 == 0) else False)
    return boolean_list
    
    
    

