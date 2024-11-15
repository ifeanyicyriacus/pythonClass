def remove_character(haystack, needle=""):

    if type(haystack) == str:
        haystack = haystack.replace(needle, "")
    elif type(haystack) == list:
        for index in range(len(haystack)):
            if needle in haystack[index]:
                haystack[index] = haystack[index].replace(needle, "")
        if "" in haystack:
            haystack.remove("")    
    return haystack
    
