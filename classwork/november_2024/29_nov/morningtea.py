def number_square(number:int) -> list:
    return [x**2 for x in range(1, number+1)]
    #return list(map(lambda x: x **2, range(1, number+1))) 
    
def get_numbers_greater_than_10(numbers:list) -> list:
    #return [x for x in numbers if x > 10]
    return list(filter(lambda x: x > 10, numbers))

def words_palindrome_checker(words:list) -> list:
    #return [x == x[::-1] for x in words]
    return list(map(lambda x: x == x[::-1], words))
    
def pluck_numbers_from(word:str) -> list:
    #return [int(x) for x in word if x.isdigit()]
    return list(map(int, filter(lambda x: x.isdigit() , word)))
    #return list(map(lambda x: pow(int(x), 3), filter(lambda x: x.isdigit() , word)))
    #return list(map(lambda x: int(x), filter(lambda x: x.isdigit(), word)))
