def higher_scorer(score_sheet:list, subject_index:int) -> list:
    name = []
    score = 0
    index = 0
    while index < len(score_sheet):
        if (score_sheet[index][subject_index] < 1) or (score_sheet[index][subject_index] > 100):
            raise ValueError
        if score < score_sheet[index][subject_index]:
            score = score_sheet[index][subject_index]
            name = [score_sheet[index][0]]
        elif score == score_sheet[index][subject_index]:
            name.append(score_sheet[index][0])
        index += 1
    return [name, score]
	
def lowest_scorer(score_sheet:list, subject_index:int) -> list:
    name = []
    score = 101
    index = 0
    while index < len(score_sheet):
        if (score_sheet[index][subject_index] < 1) or (score_sheet[index][subject_index] > 100):
            raise ValueError
        if score > score_sheet[index][subject_index]:
            score = score_sheet[index][subject_index]
            name = [score_sheet[index][0]]
        elif score == score_sheet[index][subject_index]:
            name.append(score_sheet[index][0])
        index += 1
    return [name, score]

def display_summary(score_sheet:list) -> list:
	subjects = ["Python", "Java", "Data science", "Design thinking"]
	print(f"Highest scorers:")
	for index in range(1, 5):
		result = higher_scorer(score_sheet, index)
		if len(result[0]) == 1:
			print(f"Highest scorer in {subjects[index-1]} is: {result[0][0]} - [{result[1]}]")
		if len(result[0]) > 1:
			names = ""
			for name in result[0]:
				names += name + ", "
			print(f"Highest scorers in {subjects[index-1]} are: [{names}] - [{result[1]}]")
	
	print(f"\nLowest scorers:")
	for index in range(1, 5):
		result = lowest_scorer(score_sheet, index)
		if len(result[0]) == 1:
			print(f"Lowest scorer in {subjects[index-1]} is: {result[0][0]} - [{result[1]}]")
		if len(result[0]) > 1:
			names = ""
			for name in result[0]:
				names += name + ", "
			print(f"Lowest scorers in {subjects[index-1]} are: [{names}] - [{result[1]}]")
	

def display_table(score_sheet:list) -> None:
	print()
	print("Name\tPy\tJava\tDS\tDT")
	for student_score_sheet in class_score_sheet:
		for element in student_score_sheet:
			print(element, end="\t")
		print("")
	print("\n")



class_score_sheet = [
	["Ifeanyi", 54, 20, 87, 65],
	["James", 54, 19, 87, 70],
	["Daniel", 76, 90, 87, 80],
	["Esther", 54, 90, 87, 97],
	["Ogene", 74, 90, 87, 90],
	["Ayo", 54, 90, 37, 20],
	["Chris", 54, 97, 47, 66],
	["AZed", 80, 90, 80, 21],
	["BiBi", 54, 99, 8, 20],
	["Priest", 89, 45, 87, 66]
]


#display_table(class_score_sheet)
#display_summary(class_score_sheet)
