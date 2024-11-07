"""function that take a string and return the number of vowels in string"""

def vowel_counter(text):
    counter = 0
    for letter in text:
        if letter.lower() == "a" or letter.lower() == "e" or letter.lower() == "i" or letter.lower() == "o" or letter.lower() == "u":
            counter += 1
    return counter
    
    
user_input = input("Enter your text here: ")
print(f"There are {vowel_counter(user_input)} vowels in this text")
            
