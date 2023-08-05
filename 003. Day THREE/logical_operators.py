# A and B
# A or B
# not
# Nested condition: if else inside if condition

print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif 12 <= age <= 18:
        bill = 7
        print("Please pay $7.")
    elif 45 <= age <= 55:
        bill = 0
        print(f"Price was nulled for you to {bill}")
    else:
        bill = 12
        print("Please pay $12.")

    wants_photo = input("Do you want a photo? Y or N ")
    if wants_photo == 'Y':
        bill += 3
        print(f"New price is ${bill}")
    else:
        print(f"Price is same: ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
