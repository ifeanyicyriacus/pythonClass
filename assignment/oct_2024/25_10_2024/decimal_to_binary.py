dec_number = int(input("Enter decimal number: "))
bin_number = ""

while (dec_number  > 0):
    rem = dec_number % 2
    bin_number = str(rem) + bin_number
    dec_number //= 2

print(f"Binary number: {bin_number}")
