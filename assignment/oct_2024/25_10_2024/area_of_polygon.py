import math

no_of_side = int(input("Enter the number of sides: "))
length_of_side = int(input("Enter the length of one side: "))
area_of_polygon = (no_of_side * pow(length_of_side, 2))/(4 * math.tan(math.pi/no_of_side))

print(f"The area of the polygon is: {area_of_polygon:.3}");
