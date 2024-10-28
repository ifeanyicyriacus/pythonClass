
number = int(input("Input the number (Table to be calculated): "))
terms = int(input("Input number of terms: "))
counter = 0
while (counter <= terms):
    print(f"{number} X {counter} = {number*counter}")
    counter += 1

