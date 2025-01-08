import random

operator_list = "+-*"
left_operands = []
right_operands = []
operators = []
correct_answers = []
user_answers = []
total_score = 0
NUMBER_OF_QUESTIONS = 5

def check_if_is_number(number: str) -> bool:
    if number.isdigit():
        return True
    elif ((len(number.split(".")) - 1) == 1) or ((len(number.split(".")) - 1) == 0):
            number = number.replace(".", "")
            if number.startswith("+") or number.startswith("-"):
                number = number[1:]
            if number.isdigit():
                return True
    return False

for i in range(NUMBER_OF_QUESTIONS):
    left_operands.append(random.randint(1, 10))
    right_operands.append(random.randint(1, 10))
    operators.append(random.choice(operator_list))
    
    match(operators[i]):
        case "+":
            correct_answers.append(left_operands[i] + right_operands[i])
        case "-":
            correct_answers.append(left_operands[i] - right_operands[i])
        case "*":
            correct_answers.append(left_operands[i] * right_operands[i])
    

for i in range(NUMBER_OF_QUESTIONS):
    print(f"Question {i + 1}: What is {left_operands[i]} {operators[i]} {right_operands[i]}")
    
    is_expecting_valid_input = True
    while(is_expecting_valid_input):
        answer = input("Your answer: ")
        
        if check_if_is_number(answer):
            answer = float(answer)
            is_expecting_valid_input = False
        else:
            print("\033[A\033[K\033[41mError: only digits allowed\033[0m")

    user_answers.append(answer)
    if user_answers[i] == correct_answers[i]:
        total_score += 1
        print("\033[32mCorrect!\033[0m")
    else:
        print("\033[31mFailed!!!\033[0m")
        
print("\nResult:")
print(f"\033[1mYou got {total_score}/{NUMBER_OF_QUESTIONS}\033[0m")




