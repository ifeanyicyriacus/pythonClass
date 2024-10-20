response = ""
number = float(input("Enter number: "))
largest_number = number
smallest_number = number
response = input("Do you want to continue (y/n): ")

while(response == "y"):
	number = float(input("Enter number: "))
	if (number > largestNumber): largestNumber = number
	if (number < smallestNumber): smallestNumber = number
	response = input("Do you want to continue (y/n): ")
print(f"The largest number is: {largest_number}\nThe smallest number is: {smallest_number}")
