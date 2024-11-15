def remove2nd(my_list:list = []):
    if len(my_list) >= 2:
        my_list.remove(my_list[1])
        return my_list
    else:
        return 0

