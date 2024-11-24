
counter = 0;
minimum = int(input("Enter start range: "))
maximum = int(input("Enter stop range: "))
step = int(input("Enter step: "))

for i in range( minimum, maximum):
	if (i % step == 0):
	    counter +=1

print(counter)
