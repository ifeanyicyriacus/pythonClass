#exercise 3.1
#fig03_03.py
"""Using nested control statements to analyze examination results."""

# initialize variables
passes = 0  # number of passes
failures = 0  # number of failures
# process 10 students
for student in range(10):
    # get one exam result 11  
    loop = True
    while loop:
        result = int(input('Enter result (1=pass, 2=fail): '))
        if result == 1: 
            passes = passes + 1
            loop = False
        elif result == 2:
            failures = failures + 1
            loop = False        
        
# termination phase
print('Passed:', passes)
print('Failed:', failures)
if passes > 8:
    print('Bonus to instructor')
