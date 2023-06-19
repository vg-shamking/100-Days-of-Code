# Nested condition: if else inside if condition

print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif 12 <= age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
elif height == 120:
    print("You are lucky, exactly to ride!!!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
