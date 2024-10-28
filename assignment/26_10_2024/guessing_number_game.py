import random
target_number = random.randint(1,100)

guess = int(input("Guess a number from 1-100: "))
while (guess != target_number):
    if guess > target_number:
        print("Too high, try again: ", end = "")
    elif guess < target_number:
        print("Too low, try again: ", end = "")
    guess = int(input())
print("Correct guess.")


