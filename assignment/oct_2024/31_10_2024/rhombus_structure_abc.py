char_number = int(input("Input the number: "))
char_alphabet = chr(ord("A") - 1)

for i in range(1, (char_number+1)):
    print(" "*(char_number-i), end="")
    forward = i
    reverse = ((i*2) - 1) - forward
    
    while forward > 0:
        char_alphabet = chr(ord(char_alphabet) + 1)
        print(char_alphabet, end="")
        forward -= 1
    
    while reverse >= 0:
        if reverse != 0:
            char_alphabet = chr(ord(char_alphabet) - 1)
            print(char_alphabet, end="")
            reverse -= 1
        else:
            char_alphabet = chr(ord(char_alphabet) - 1)
            break
    print()

for i in range((char_number-1), 0, -1):
    print(" "*(char_number-i), end="")
    
    forward = i
    reverse = ((i*2) - 1) - forward
    
    while forward > 0:
        char_alphabet = chr(ord(char_alphabet) + 1)
        print(char_alphabet, end="")
        forward -= 1
    
    while reverse >= 0:
        if reverse != 0:
            char_alphabet = chr(ord(char_alphabet) - 1)
            print(char_alphabet, end="")
            reverse -= 1
        else:
            char_alphabet = chr(ord(char_alphabet) - 1)
            break
    print()
