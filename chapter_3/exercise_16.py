#exercise 3.16 (Nested Control Statements)
largest_1 = 0
largest_2 = 0

for count in range(10):
    number = int(input("Enter a number: "))
    if count == 0:
        largest_1 = number
        print(f"The largest values is: {largest_1}")
        continue
        
    if count == 1 and number > largest_1:
        largest_2 = largest_1
        largest_1 = number
        continue
    elif count == 1 and largest_1 >= number:
        largest_2 = number
        continue
    
    if count >= 2:
        if number > largest_1:
            largest_2 = largest_1
            largest_1 = number
        elif number <= largest_1 and number >= largest_2:
            largest_2 = number
        print(f"The 1st and 2nd largest values are: {largest_1} and {largest_2} respectively")
print(f"The 1st and 2nd largest values are: {largest_1} and {largest_2} respectively")
