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
    if not(type(investment_amount) in [int, float]) or not(type(monthly_interest_rate) in [int, float]) or not(type(year) in [int, float]):
        raise TypeError
    elif investment_amount < 0 or monthly_interest_rate < 0 or year < 0:
        raise ValueError
    else:
        no_of_months = year * 12
        future_investment_amount = investment_amount * (1 +  monthly_interest_rate) ** no_of_months
        return round(future_investment_amount, 2)
        

def only_floats(a=None, b= None):
    if a == None or b == None or type(a) is str or type(b) is str:
        raise TypeError
    result = 0
    if type(a) == float and type(b) == float:
        result += 2
    elif type(a) == float or type(b) == float:
        result += 1
    return result
    

def my_discount(price=None, discount=None):
    if type(price) in [int, float] and type(discount) in [int, float]:
        if price >= 0 and discount >= 0:
            discount_amount = price * (discount / 100)
            my_discount = price - discount_amount
            return round(my_discount, 2)
        else:
            raise ValueError
    elif price == None or discount == None:
        raise TypeError    
    else:
        raise TypeError
