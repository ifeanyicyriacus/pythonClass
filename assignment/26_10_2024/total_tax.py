EARNING_CEILING = 30000
NORMAL_TAX_RATE = 15.0 / 100.0
EXCESS_TAX_RATE = 20.0 / 100.0

earnings = float(input("Enter your total earnings: "))
excess_earnings = earnings - EARNING_CEILING
total_tax = 0

if excess_earnings <= 0:
    total_tax = earnings * NORMAL_TAX_RATE
else:
    total_tax = EARNING_CEILING * NORMAL_TAX_RATE
    total_tax += (excess_earnings * EXCESS_TAX_RATE)
print(f"The total tax payable: {total_tax}")
