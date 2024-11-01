"""38. program to check for increasing or decreasing order from three inputs """

number_1 = int(input("Enter number: "))
number_2 = int(input("Enter another number: "))
number_3 = int(input("Enter another number: "))

if number_1 > number_2 and number_2 > number_3:
	print("Numbers are arranged in decreasing order")
elif number_1 < number_2 and number_2 < number_3:
	print("Numbers are arranged in increasing order")
else:
	print("Numbers are in no particular order")
