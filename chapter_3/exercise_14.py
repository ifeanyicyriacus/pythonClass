#exercise 3.14 (Approximating the Mathematical Constant PI)

pi = 4
counter = 1
value = 3
test_a = test_b = test_c = True
while True:
    if counter%2 != 0:
        pi -= (4/value)
    else:
        pi += (4/value)

    if test_a and round(pi, 2) == 3.14:
        print(f"At series {counter:>7} PI is {pi:<10.2f}")
        test_a = False
    if test_b and round(pi, 3) == 3.141:
        print(f"At series {counter:>7} PI is {pi:<10.3f}")
        test_b = False
    if test_c and round(pi, 4) == 3.1415:
        print(f"At series {counter:>7} PI is {pi:<10.4f}")
        test_c = False
    if round(pi, 5) == 3.14159:
        print(f"At series {counter:>7} PI is {pi:<10.5f}")
        break
    counter += 1
    value += 2
    
#At series     151 PI is 3.14      
#At series     915 PI is 3.141     
#At series    7009 PI is 3.1415    
#At series  130657 PI is 3.14159   

