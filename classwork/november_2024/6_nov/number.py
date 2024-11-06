
length = int(input("Enter number: "))
for number in range (1, length+1):
	for number2 in range(1, number+1):
		print(number2, end="")
	print()
print("hello")
for number in range (length, 1, -1):
    for number2 in range(1, number):
	    print(number2, end="")
    print()


