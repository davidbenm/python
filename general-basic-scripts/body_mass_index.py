height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
height_float = float(height)
weight_float = float(weight)
BMI = int(weight_float/(height_float**2)) #formula to calculate bmi
print("Your BMI is: " + str(BMI))
