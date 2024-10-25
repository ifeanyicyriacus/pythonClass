POUND_TO_KG_CONSTANT = 0.45359237
INCH_TO_METRE_CONSTANT = 0.0254
weight_in_pound = float(input("Enter weight (in pounds): "))
height_in_inch = float(input("Enter height (in inches): "))
weight_in_kg = weight_in_pound * POUND_TO_KG_CONSTANT
height_in_metre = height_in_inch * INCH_TO_METRE_CONSTANT

bmi = weight_in_kg / pow(height_in_metre, 2)
print(f"The BMI is: {bmi}/n");
