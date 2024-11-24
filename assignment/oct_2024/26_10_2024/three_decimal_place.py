number1 = float(input("Input floating-point number: "))
number2 = float(input("Input another floating-point number: "))

difference = abs(max(number1, number2) - min(number1, number2))
if difference < 0.001:
    print("They are the same")
else:
    print("They are different")
