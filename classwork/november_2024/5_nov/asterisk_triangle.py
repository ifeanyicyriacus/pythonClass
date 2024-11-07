"""program to print a triangle using asterisk"""
for row in range(1, 6):
	for column in range(row):
		print("*", end="")
	print()
print()
#or
for row in range(1, 6):
    print("*" * row)
print()

