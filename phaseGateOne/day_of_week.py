DAYS_OF_WEEK = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]

today_day = 0 
while(True):
    today_day = input("Enter today's day: ")
    if today_day.isdigit() and (int(today_day) >= 0 and int(today_day) <= 6) :
        today_day = int(today_day)
        break
    else:
        print("Invalid input: (Enter an integer from 0 - 6 ), TRY AGAIN!")
print(f"You just selected {DAYS_OF_WEEK[today_day]}")

future_day = 0 
while(True):
    future_day = input("Enter the number of days elapsed since today: ")
    if future_day.isdigit() and int(future_day) >= 0 :
        future_day = int(future_day)
        break
    else:
        print("Invalid input: (Enter an integer greater than 0 ), TRY AGAIN!")

total = today_day + future_day

print(f"The future day is on {DAYS_OF_WEEK[total % 7]} ")
