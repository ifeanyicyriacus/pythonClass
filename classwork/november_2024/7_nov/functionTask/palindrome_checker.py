def palindrome_checker(text):
    index = -1
    for letter in text:
        if letter != text[index]:
            return False
        index -= 1
    return True
    
"""method 2"""
def palindrome_checker_2(text):
    counter = 0
    counter_2 = -1
    while (counter <= len(text)//2):
        print(text[counter])
        print(text[counter_2])
        if text[counter] != text[counter_2]:
            return False
        counter += 1
        counter_2 += -1
    return True

"""method 3"""
def palindrome_checker_3(text):
    text_reversed = text[::-1]
    if text != text_reversed:
        return False
    return True

print("Palindrome checker")
text = input("Enter your text here: ")
print(f"'{text}' {'is a palindrome' if palindrome_checker(text) else 'is not a palindrome'}")
print(f"'{text}' {'is a palindrome' if palindrome_checker_2(text) else 'is not a palindrome'}")
print(f"'{text}' {'is a palindrome' if palindrome_checker_3(text) else 'is not a palindrome'}")


