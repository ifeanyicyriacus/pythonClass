
choice = "y"
while(choice.lower() == "y"):
	number1 = float(input("Enter number 1: "))
	number2 = float(input("Enter number 2: "))
	sum = number1 + number2
	print(f"Their sum is: {sum}")
	
	choice = input("Do you still wish to repeat the operation (y/n): ")
	
