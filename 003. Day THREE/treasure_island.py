print("Welcome to Treasury Island")
print("Your mission is to find treasury")
first_turn = input("You are at a cross road. Where do you want to turn?\nLeft: L\nRight: R\n")
if first_turn == "L":
    print("There is a lazy lion. You're alive.")
    next1 = input("Do you want to hug lion? Y or N\n")
    if next1 == "Y":
        print("Lion allowed you to go. You found treasures")
        last = input("Are you happy? Y or N\n")
        if last == "N":
            print("You can take it all and spend as you wish")
        else:
            print("Money not give happiness. You lost")
    else:
        print("Lion is awake and ate you.")
elif first_turn == "R":
    print("There is a river.")
    next2 = input("There are crocodiles. Are you afraid? Y or N\n")
    if next2 == "Y":
        print("How can you be afraid if you have an aligator knife.")
    else:
        print("Croco felt fear and ate you.")
else:
    print("You died. Game Over")
