#exercise 3.18 (Nexted Looping)

print(f'{"(a)":<10}   {"(b)":<10}   {"(c)":<10}   {"(d)":<10}')
for counter_b in range(1, 11):

    for counter_a in range(1, (counter_b + 1)):
        print("*",end = "")
    for counter_a in range(1, (11 - counter_b)):
        print(" ",end = "")
    print("   ", end = "")
    
    for counter_a in range(1, (12 - counter_b)):
        print("*",end = "")
    for counter_a in range(1, counter_b):
        print(" ",end = "")
    print("   ", end = "")
    
    for counter_a in range(1, counter_b):
        print(" ",end = "")
    for counter_a in range(1, (12 - counter_b)):
        print("*",end = "")
    print("   ", end = "")    
    
    for counter_a in range(1, (11 - counter_b)):
        print(" ",end = "")
    for counter_a in range(1, (counter_b + 1)):
        print("*",end = "")
    print("   ", end = "")  
    print()



