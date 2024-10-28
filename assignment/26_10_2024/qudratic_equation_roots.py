import math
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

discriminant = pow(b, 2) - 4*a*c
if a == 0:
    print("There are no roots when a = 0")
elif discriminant > 0:
    root_1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root_2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"The roots are {root_1} and {root_2}")
elif discriminant == 0:
    root = (-b + math.sqrt(discriminant)) / (2 * a)
    print(f"The root is {root}")
else:
    real_root = -b / (2 * a)
    imaginary_unit = 1 / (2 * a)
    print(f"The roots are {real_root}+{imaginary_unit}i and {real_root}-{imaginary_unit}i")
