# That's BMI calculator
#
height = input("What is your height in m?: ")
weight = input("What is your weight in kg?: ")

bmi = float(weight) / (float(height) ** 2)  # BMI = (weigth (kg)) / (height**2(m**2))
print(int(bmi))
