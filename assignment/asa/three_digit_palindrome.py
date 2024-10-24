number = int(input("Enter a three digit number: "))
hundreds = number // 100
units = number % 10

if (hundreds == units):
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")
