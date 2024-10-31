i = 1
while i <= 10:
	k = 1
	j = 1
	while j <= 5:
		if i%4 == 0:
			print(pow(i, k), end =" ")
			k += 1
		j += 1
	i += 1
print()
