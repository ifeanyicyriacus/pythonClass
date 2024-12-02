import random

number_1 = random.randrange(1, 101)
number_2 = random.randrange(1, 101)

sentinel = -1
while sentinel == -1:
    user_guess = input("Guess the sum of two integer inder 100: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        sentinel = 0
    else:
        print("Invalid input try again")

total = number_1 + number_2
if user_guess == total:
    print(True)
else:
    print(False)
