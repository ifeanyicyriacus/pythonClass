number = int(input("Enter a number: "))
largest = number
smallest = number

choice = input("Do you want to continue (y/n)? ")
while(choice == "y"):
    number = int(input("Enter a number: "))
    if number > largest:
        largest = number
    elif number < smallest:
        smallest = number
    choice = input("Do you want to continue (y/n)? ")


print(f"Largest: {largest}")
print(f"Smallest: {smallest}")
    
    
