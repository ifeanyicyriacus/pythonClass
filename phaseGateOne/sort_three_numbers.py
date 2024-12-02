numbers = []
count = 0
while count < 3:
    number = input(f"Enter number {count+1}: ")
    if number.isdigit():
        numbers.append(int(number))
        count += 1
    else:
        print("Invalid input, try again")
sorted_numbers = sorted(numbers)
print(sorted_numbers[0], sorted_numbers[1], sorted_numbers[2], sep = ",")
