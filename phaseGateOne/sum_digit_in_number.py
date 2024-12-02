sentinel = -1
while sentinel == -1:
    number = input("Enter a number between 0 and 1000: ")
    if number.isdigit() and int(number) >=0 and int(number) <= 1000:
        sentinel = 0
    else:
        print("Invalid input: Try again")
    
print("sum: ", sum([int(x) for x in number]))

