"""produce a multiplication table for any number given by a user"""

number = int(input("Enter the multiplication table you want: "))

for count in range(1,11):
	print(f"{number} x {count:<2} = {number * count}")
	
	
