number = int(input("Enter an integer between 0 and 1000: "))
hundreds = number // 100
tens = (number // 10) % 10
units = number % 10
sum_of_digits = hundreds + tens + units
print(f"The sum of the digits is {sum_of_digits}")
