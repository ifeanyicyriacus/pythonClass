counter_b = 1
while (counter_b <= 9):
	counter_a = 1
	while(counter_a <= 9):
		print(f"{counter_a} * {counter_b} = {counter_a * counter_b}\t", end = "")
		counter_a += 1
	print()
	counter_b += 1
