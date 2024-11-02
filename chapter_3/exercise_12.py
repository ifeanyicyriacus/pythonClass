#exercise 3.12 (Palindromes)

number = int(input("Enter a five-digit integer: "))
digit_a = (number //10000)%10
digit_b = (number //1000)%10

digit_d = (number //10)%10
digit_e = (number //1)%10

if(digit_a == digit_e and digit_b == digit_d):
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")
