import random

names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
print(names)
print(len(names))
payer = names[random.randint(0, len(names))]
print(f"{payer} is going to pay today!")
