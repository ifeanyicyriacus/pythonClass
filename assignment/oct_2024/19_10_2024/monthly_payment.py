principal = float(input("Enter the principal amount: $"))
annual_rate = float(input("Enter the annual interest rate: "))
duration = float(input("Enter the duration in years: "))

monthly_rate = annual_rate / (100 * 12)
no_of_months = duration * 12

monthly_payment = (principal * (monthly_rate * (1 + monthly_rate) ** no_of_months)) / (((1 + monthly_rate) ** no_of_months) - 1)

print(f"Your monthly payment is ${monthly_payment}")
