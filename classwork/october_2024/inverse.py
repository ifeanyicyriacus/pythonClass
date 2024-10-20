#program that takes  a number from 100 - 999 and print the inverse of the number with spaces inbetween

number = int(input("Enter a number between 100 - 999\n"))
firstDigit = number//100
secondDigit = (number //10) % 10
thirdDigit = number%10
odd = 0
even = 0
if (firstDigit%2 == 0): even = even + 1
if (secondDigit%2 == 0): even = even + 1
if (thirdDigit%2 == 0): even = even + 1

if (firstDigit%2 != 0): odd = odd + 1
if (secondDigit%2 != 0): odd = odd + 1
if (thirdDigit%2 != 0): odd = odd + 1

print(thirdDigit," ", secondDigit," ", firstDigit,"\n")
print("odd number are: ", odd)
print("Even number are: ", even)
