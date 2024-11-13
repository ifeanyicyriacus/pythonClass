from math import sqrt

def divide_or_square(number):
    number = float(number)
    remainder = number % 5
    if remainder == 0.0:
        if number > 0:
            return round(sqrt(number), 3)
        else:
            raise ValueError
    else:
        return round(remainder, 3)

def future_investment_amount(investment_amount = 0, monthly_interest_rate = 0, year = 0):
    no_of_months = year * 12
    future_investment_amount = investment_amount * (1 +  monthly_interest_rate) ** no_of_months
    return round(future_investment_amount, 2)
    
    
    

print(future_investment_amount())

