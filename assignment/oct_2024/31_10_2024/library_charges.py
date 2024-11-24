"""34. program to determine the appropriate response given a number of days of holding book after return date """

number_of_days = int(input("Enter the number of days (after duedate) it took to return the book: "))

if number_of_days >= 30:
	print("The member's membership will be cancelled")
elif number_of_days >= 10:
	print("The member should be fined 5 rupees")
elif number_of_days >= 6:
	print("The member should be fined 1 rupee")
elif number_of_days == 5:
	print("The member should be fined 50 paise")
else:
	print("The member should not be fined")
