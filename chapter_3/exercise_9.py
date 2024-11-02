#exercise 3.9

number = int(input("Enter a five-digit integer: "))
for power in range(4, -1, -1):
    digit = (number //10**power)%10
    print(digit, end="     ")
    
print()



