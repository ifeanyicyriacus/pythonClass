str_number = input("Enter the number: ")
sum = 0

for str_digit in str_number:
    digit = int(str_digit)
    if digit >= 5:
        sum = sum + 1
print(sum)
