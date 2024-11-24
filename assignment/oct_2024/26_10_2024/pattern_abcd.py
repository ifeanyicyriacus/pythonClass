counter_a = 1
counter_b = 1

print("Pattern A\tPattern B\t Pattern C\tPattern D")
while(counter_b <=6):
    counter_a = 1
    while(counter_a <= 4):
        if counter_a <= 1:
            print(f"{"* " * counter_b}",end = "")
            print(f"{"  " * (6 - counter_b)}",end = "")
        elif counter_a <= 2:
            print(f"{"* " * (7 - counter_b)}",end = "")
            print(f"{"  " * (counter_b - 1)}",end = "")
        elif counter_a <= 3:
            print(f"{"  " * (6 - counter_b)}",end = "") 
            print(f"{" *" * counter_b}",end = "")
        else:
            print(f"{"  " * (counter_b - 1)}",end = "")
            print(f"{" *" * (7 - counter_b)}",end = "")
        print("\t", end = "")
        counter_a += 1
    print()
    counter_b += 1
