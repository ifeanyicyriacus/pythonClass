#exercise 3.22 (Optional Clause of a loop)
for i in range(2):
    value = int(input("Enter an integer (-1 to break): "))
    print("You entered: ", value)
    
    if value == -1:
        break
else:
    print("The loop terminates without executing the break")

#Confirmed
