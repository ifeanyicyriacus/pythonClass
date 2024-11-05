count_a = count_b = 5
while count_b != 0:
    print(count_a, end = "")
    count_a -= 1
    if count_a == 0:
        count_b -= 1
        count_a = count_b
        print()


        
