positives_count = negatives_count = zeros_count = 0
for count in range(1, 6):
    number = float(input(f"Enter number {count}: "))
    if number > 0:
        positives_count += 1
    elif number < 0:
        negatives_count += 1
    else:
        zeros_count += 1
print(f"\nPositive numbers: {positives_count}")
print(f"Negative numbers: {negatives_count}")
print(f"Zeros: {zeros_count}")

