"""Number1 raise to power number2"""
base = float(input("Enter the 1st number: "))
exponent = float(input("Enter the 2nd number: "))
result = base
counter = 2
if (exponent == 0): result = 1
else:
    while (counter <= abs(exponent)):
        result *= base
        counter += 1
if (exponent < 0): result = 1 / result
print(f"{base} raised to power {exponent} = {result}\n")

