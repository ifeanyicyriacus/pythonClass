from random import randrange

def quiz():
    answers = []
    questions = []
    responses = []
    total = 0

    for index in range(10):
        first_operand = randrange(1, 1001)
        second_operand = randrange(1, 1001) 
        operator = ["+","+","+","+","+", "*","*","*", "-","-"]
        question = str(first_operand) + operator[index] + str(second_operand)
        if operator[index] == "+":
            answer = first_operand + second_operand
        elif operator[index] == "*":
            answer = first_operand * second_operand
        else:
            answer = first_operand - second_operand
        questions.append(question)
        answers.append(answer)
        
        
    for index in range(10):
        response = int(input(f"Q{index+1}.\tWhat is: {questions[index]}? \n\t>>> "))
        responses.append(response)
        if answers[index] == response:
            total += 1

    print(f"\nResult: you got {total}/10\n")

    if total < 10:
        for index in range(10):
            if answers[index] != responses[index]:
                print(f"Q{index+1}\tWhat is: {questions[index]}? ")
                print(f"You answered wrongly: {responses[index]}")
                print(f"The correct answer is: {answers[index]}")
                print()
     
     
quiz()
