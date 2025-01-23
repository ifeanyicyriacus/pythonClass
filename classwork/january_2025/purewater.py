def find_index(number_list:list, keyword:int) -> str:
    for i in range(len(number_list)):
        if number_list[i] == keyword:
            return "index " + str(i)
    return "not available"
    
    
def positive_negative_and_zeros_count(number_list:list) -> str:
    zeros = 0
    positives = 0
    negatives = 0
    
    for number in number_list:  
        if number < 0:
            negatives += 1
        elif number > 0:
            positives += 1
        else:
            zeros += 1
    return f"positives: {positives}\nnegatives: {negatives}\nzeros: {zeros}"
    
    
    
