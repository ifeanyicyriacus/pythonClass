#weight = float(input("Enter your weight (in Kg): "))
#height = float(input("Enter your height (in metres): "))
#body_mass_index = weight / pow(height, 2)
body_mass_index = float(input("Enter your bmi: "))
BMI_MAX_INDEX = 29.9
BMI_MID_INDEX = 25.0
BMI_MIN_INDEX = 18.5

if (body_mass_index > BMI_MAX_INDEX):
    print("You are obese")
elif (BMI_MAX_INDEX >= body_mass_index >= BMI_MID_INDEX):
    print("You are over weight")
elif (BMI_MID_INDEX >= body_mass_index >= BMI_MIN_INDEX):
    print("You have normal weight")
else:
    print("You are under weight")
