"""A function that prints the acronomy of the string"""

def acronym_in_text(text):
    acronym = ""
    previous_letter_is_a_whitespace = True
    for letter in text:
        if previous_letter_is_a_whitespace:
            acronym += letter
            previous_letter_is_a_whitespace = False
        if letter == " ":
            previous_letter_is_a_whitespace = True
            
    return acronym.upper()
    
print("Text to Acronym printer")
user_input = input("Enter your text here: ")
print(f"{acronym_in_text(user_input)}")
            
