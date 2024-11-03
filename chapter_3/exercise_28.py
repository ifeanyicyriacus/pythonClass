#exercise 3.28 (Intro to Data Science: Mean, Median and Mode)
from statistics import mean, median, mode

sample_1 = [9, 11,22, 34, 17, 22, 34, 22, 40]
sample_2 = [9, 11,22, 34, 17, 22, 34, 22, 40, 34]

print()
print("mean: ", mean(sample_1))
print("median: ", median(sample_1))
print("mode: ", mode(sample_1))
print()
print("mean: ", mean(sample_2))
print("median: ", median(sample_2))
print("mode: ", mode(sample_2))


#after i added '34' the mode did not stil change, it picked the first highest frequency in ascending order
