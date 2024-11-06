def is_prime(number):
    for test_number in range(2, abs(number)):
        if number % test_number == 0:
            return False
    return True
    
    
number = int(input("Enter a number to check if prime or not: "))
if is_prime(number):
    print(f"Number ({number}) is a prime number.")
else:
    print(f"Number ({number}) is not a prime number.")
    
