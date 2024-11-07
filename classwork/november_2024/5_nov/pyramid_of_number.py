no_of_lines = int(input("Enter number of lines: "))

for number in range(1, (no_of_lines + 1)):
    print(" " * (no_of_lines - number), end="")
    counter = number
    while counter >= 1:
        print(counter, end="")
        counter -= 1
    counter += 2
    while counter <= number:
        print(f"{counter}", end="")
        counter += 1
    print()
    
