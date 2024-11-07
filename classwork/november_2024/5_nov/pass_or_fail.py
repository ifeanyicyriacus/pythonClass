"""Program to count the number of stuudent who passes and fails from 15 scores"""

passes = 0
fails = 0
for count in range(1, 16):
	score = int(input(f"Enter score of student ({count:>2}): "))
	if score >= 45:
		passes += 1
	else:
		fails += 1

print(f"\n{passes} student(s) passed\n{fails} student(s) failed\n")
