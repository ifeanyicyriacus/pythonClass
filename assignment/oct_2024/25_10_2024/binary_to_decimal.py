binary_number = int(input("Enter Binary number: "))
decimal_number = 0
power = 0
crop_1 = 10
crop_2 = 1
NUMBER_BASE = 2

while binary_number / crop_2 > 0:
    digit = (binary_number % crop_1) // crop_2
    value = digit * pow(NUMBER_BASE, power)
    
    decimal_number += value
    crop_1 *= 10
    crop_2 *= 10
    power += 1

print(f"Binary ({binary_number}) is decmal ({decimal_number})")
