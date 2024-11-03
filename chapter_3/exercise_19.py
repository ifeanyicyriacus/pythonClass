#exercise 3.19 (Brute-Force Computing Pythagorean Triples)
print("Side A\tSide B\tHypotenuse")

for side_a in range(1, 21):
    for side_b in range(1, 21):
        for side_c in range(1, 21):
            if pow(side_a, 2) + pow(side_b, 2) == pow(side_c, 2):
                print(f"{side_a}\t{side_b}\t{side_c}")

