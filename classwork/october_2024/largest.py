count = 1
largest = 0
while(count >=1 and count <= 10):
    number = int(input("Enter the number: "))
    if (number >= 1 and number <= 100):
        if largest < number:
            largest = number
        count += 1	    
    else:
        print("Invalid input")
print(largest)
