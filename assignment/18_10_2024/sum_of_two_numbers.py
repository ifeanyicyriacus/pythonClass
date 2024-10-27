"""sum of two numbers"""
decision = "y"
sum = 0
while (decision == "y"):
	number = float(input("Enter first number: "))
	sum = number
	number_2 = float(input("Enter second number: "))
	sum += number
	print(f"The sum is: {sum}\n")
	decision = input("Do you wish to perform the operation again (y/n)")
