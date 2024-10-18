#exercise 2.15 (Sort in ascending order)

num1 = float(input("Enter a floating number: "))
num2 = float(input("Enter a another floating number: "))
num3 = float(input("Enter a another floating number: "))

temp = 0
if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp
if num1 > num3:
    temp = num1
    num1 = num3
    num3 = temp
if num2 > num3:
    temp = num2
    num2 = num3
    num3 = temp
print(num1,"  ", num2, "  ", num3)
    
