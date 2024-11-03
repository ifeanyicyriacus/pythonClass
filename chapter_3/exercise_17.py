#exercise 3.17 (Nexted Loops)
print("\n(a)")
for counter_b in range(1, 11):
    for counter_a in range(1, (counter_b + 1)):
        print("*",end = "")
    print()
    
print("\n(b)")
for counter_b in range(10, 0, -1):
    for counter_a in range(1, (counter_b + 1)):
        print("*",end = "")
    print()

print("\n(c)")
for counter_b in range(10, 0, -1):
    for counter_a in range(0, (10 - counter_b)):
        print(" ",end = "")
    for counter_a in range(1, counter_b+1):
        print("*",end = "")  
    print()

print("\n(d)")
for counter_b in range(1, 11):
    for counter_a in range(0, (10 - counter_b)):
        print(" ",end = "")
    for counter_a in range(1, (counter_b + 1)):
        print("*",end = "")  
    print()
