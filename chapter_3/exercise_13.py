#exercise 3.13 (Factorials)

number = int(input("Enter an +ve integer to calculate the factorial: "))
result = 1
if number > 0:
    for value in range(1, (number+1)):
        result *= value
else:
    print("Enter a integer greater than 0")
    
print(f"factorial of {number} is {result}")

#it could not give me the factorial of this number 10000200002022
