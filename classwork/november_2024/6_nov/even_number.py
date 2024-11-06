def even_number_counter(number):
    no_of_even = 0
    for test_number in range(1, abs(number)):
        if test_number % 2 == 0:
            no_of_even += 1
    return no_of_even
number2 = int(input("""\nEnter a number to check the count of even numbers between the zero and the number: """))

print(f"There are ({even_number_counter(number2)}) even numbers between 0 and {number2}")    

