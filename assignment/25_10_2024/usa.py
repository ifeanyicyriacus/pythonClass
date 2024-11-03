row = 1
while row <=5:
    temp_counter_1 = 1
    while temp_counter_1 <= 6:
        if row %2 != 0:
            print("* ", end="")
        else:
            print(" *", end="")
        temp_counter_1 += 1
        
    temp_counter_2 = 1
    while temp_counter_2 <= 34:
        print("-", end="")
        temp_counter_2 += 1
    print()
    row += 1

while row <= 11:
    temp_counter_3 = 1
    while temp_counter_3 <= 46:
        print("-", end="")
        temp_counter_3 += 1
    print()
    row += 1
    
    
    

