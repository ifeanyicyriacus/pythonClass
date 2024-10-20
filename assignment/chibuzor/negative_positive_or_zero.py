"""negative, positive and zero numbers"""
counter = 1
positiveCount = 0
negativeCount = 0
zeroCount = 0

while (counter <=5):
    number = float(input("Enter the number: "))
    if number > 0:
        positiveCount += 1
    elif number < 0:
        negativeCount += 1
    else:
        zeroCount += 1
    counter += 1
print(f"\nPositive numbers: {positiveCount}\nNegativeNumbers: {negativeCount}\nZeros: {zeroCount}\n")
        
