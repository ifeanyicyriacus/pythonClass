i = 1
while i <= 10:
    j = 1
    while j <= 5:
        if i%4 == 0:
            print(i, end ="")
        j += 1
    if i%4 == 0:
        print(" ", end = "")
    i += 1
print()    
