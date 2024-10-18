#exercise 2.11 (Separating the digit in an Integer)

number = int(input("Enter a five-digit integer: "))
12345 
digit1 = (number // 10000)
digit2 = (number // 1000) %10
digit3 = (number // 100) %10
digit4 = (number // 10) %10
digit5 = (number % 10)

print(digit1,"   ", digit2,"   ", digit3,"   ", digit4,"   ", digit5)


