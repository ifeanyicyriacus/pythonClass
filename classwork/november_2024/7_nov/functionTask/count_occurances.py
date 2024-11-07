def count_occurances(keyword, text):
    keyword_occurances = 0
    for letter in text:
        if keyword == letter:
            keyword_occurances += 1
    return keyword_occurances
    
print("Text to Acronym printer")
text = input("Enter your text here: ")
character = input("Enter your character to search for: ")
print(f"'{character}' appears ({count_occurances(character, text)}) times")
            

