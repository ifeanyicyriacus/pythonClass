#exercise 3.11 (Miles per Gallon)

total_gallons = float(input("Enter the gallons used (-1 to end): "))
total_miles = float(input("Enter the miles driven: "))
print(f"The miles/gallon for this tank was {total_miles/total_gallons}")
gallons = 0
while(gallons != -1):
    gallons = float(input("Enter the gallons used (-1 to end): "))
    if gallons == -1:
        break
    miles = float(input("Enter the miles driven: "))
    print(f"The miles/gallon for this tank was {miles/gallons}")
    total_miles += miles
    total_gallons += gallons
    
overall_average = total_miles / total_gallons
print(f"The overall average miles/gallon was {overall_average:>.6f}")

    
    
