"""2.18 print a table"""
print("a\tb\tpow(a, b)")
counter = 1
while(counter <= 5):
	counter_b = counter + 1
	print(f"{counter}\t{counter_b}\t{pow(counter, counter_b)}")
	counter += 1
