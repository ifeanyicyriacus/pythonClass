dec_number = int(input("Enter decimal number: "))
bin_number = ""

while (dec_number  > 0):
    rem = dec_number % 2
    bin_number = rem + bin_number
    dec_number /= 2

System.out.printf(f"Binary number: {bin_number}%n")
