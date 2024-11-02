#exercise 3.8
#exercise 2.10 (Arithematic, Smallest and largest)

counter = 0
total = 0
minimum = 0
maximum = 0
product = 1
temp = 0
number = 0
number_1 =0
number_2 = 0
number_3 = 0
while counter < 4:
    number = int(input("Enter the another integer: "))
    total += number
    product *= number
        
    if counter == 0:
        maximum = number
        minimum = number
    else:
        maximum = max(maximum, number)
        minimum = min(minimum, number)
    temp = number
    counter += 1

print("Their sum is: ", total)
print("Their average is: ", total / counter)
print("Their product is: ", product)
print("The smallest is: ", minimum)
print("Their largest is: ", maximum)
