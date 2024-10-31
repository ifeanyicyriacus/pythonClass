sum = 0
i = 1
while i <= 10:
	k = 1
	j = 1
	while j <= 5:
		if i%4 == 0:
			sum += pow(i, k)
			k += 1
		j += 1
	i += 1
if sum != 0:
	print(sum)
