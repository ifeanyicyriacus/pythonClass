def sum_of_multiples(x, n):
    counter = 1
    sum = 0
    while(x * counter) < n:
        sum += (x * counter)
        counter += 1
    return sum
    

print("Sum of multiples")
input_x = int(input("Enter the value of  x: "))
input_n = int(input("Enter the value of  n: "))
print(f"the sum of multiples of ({input_x}) that are less then ({input_n}) are ({sum_of_multiples(input_x, input_n)})")
