import time
import random

score_counter = 0
operands_list = []

count = 1
while count <= 10:
    r_operand = random.randrange(1, 50)
    l_operand = random.randrange(1, 50)
    if r_operand >= l_operand:
        operands_list.append([r_operand, l_operand])
        count += 1

print("Test begin now ...")
start_timer = time.time()

counter = 0
while counter < len(operands_list):
    r_operand = operands_list[counter][0]
    l_operand = operands_list[counter][1]
    
    answer = input(f"Ques{counter+1:>2}. What is {r_operand:>2} - {l_operand:>2}? ")
    if answer.isdigit():
        answer = int(answer)
    else:
        print("invalid input: Next question")
        counter += 1
        continue
    if answer == (r_operand - l_operand):
        score_counter += 1
    counter += 1
    
stop_timer = time.time()
time_taken = stop_timer - start_timer
print(f"you got {score_counter} questions correctly")
print(f"You spent a total of {time_taken:.0f} seconds, taking the test.")
