#exercise 3.10 (7% Investment Return)
from decimal import Decimal
principal = Decimal('1000.00')
rate = Decimal('0.07')

for no_of_years in range (1, 31):
    balance = principal * (1 + rate)**no_of_years
    print(f"After year {no_of_years:>2} the ROI is: {balance:>10.2f}")
