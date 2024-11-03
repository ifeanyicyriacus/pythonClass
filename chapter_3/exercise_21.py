#exercise 3.21 (Change using fewest number of coins)
DOLLAR = 100
QUARTER = 25
DIME = 10
NICKEL = 5
PENNY = 1

number = DOLLAR - int(input("Enter price of the item: "))
quarters = number // QUARTER
number %= QUARTER
dimes = number // DIME
number %= DIME
nickels = number // NICKEL
number %= NICKEL
pennies = number // PENNY

print("Your change is:")
print(f"{quarters} quarters\n" if quarters > 0 else "", end="")
print(f"{dimes} dimes\n" if dimes > 0 else "", end="")
print(f"{nickels} nickels\n" if nickels > 0 else "", end="")
print(f"{pennies} pennies\n" if quarters > 0 else "", end="")
