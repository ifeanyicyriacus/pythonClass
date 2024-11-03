#exercise 3.15 (Approximating the Mathematical Constant e)
# e = 1 + (1/1!) + (1/2!) + (1/3!) + ... + (1/10!)

e = 1
for count in range(1, 11):
    product = 1
    for value in range(1, count+1):
        product *= value
    
    e += 1/product

print(f"Value of e is: {e}")

#Value of e is: 2.7182818011463845

