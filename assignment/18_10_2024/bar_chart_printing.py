output = ""
counter = 1
while (counter <= 5):
    exponent = int(input("Enter the number: "))
    temp_counter = 1
    asterisks = ""
    while (exponent >= temp_counter):
        asterisks += "*"
        temp_counter += 1
    output += asterisks + "\n"
    counter += 1    
print(output)
