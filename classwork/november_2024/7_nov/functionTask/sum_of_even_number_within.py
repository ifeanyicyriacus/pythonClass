"""create a function that accepts an integer n and return the sum of all even number from from 1 to n"""

def sum_of_even_number_within(number:int):
	sum = 0
	for count in range(1, number+1):
		if count % 2 == 0:
			sum += count
	return sum
	

print("Function to sum the even numbers between 1 and an integer")
user_input = int(input("Enter an integer: "))
print(f"The sum of even number from (1 & {user_input}) is: {sum_of_even_number_within(user_input)}")
