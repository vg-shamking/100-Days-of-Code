# That's BMI calculator
#
height = float(input("What is your height in m?: "))
weight = float(input("What is your weight in kg?: "))

bmi = round(weight / (height ** 2)) # BMI = (weight (kg)) / (height**2(m**2))
print(int(bmi))
if bmi < 18.5:
    print(f"Your bmi is {bmi}, and you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, and that's normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, and that's overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, and that's obese.")
else:
    print("Something went wrong")
