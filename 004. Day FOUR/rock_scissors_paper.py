import random

rock = '''
    _________
___'    _____)
        (______)
        (______)
        (_____)
___.___(___)
'''

paper = '''
    _________
___'    _____)____
        (__________)
        (__________)
        (_________)
___.___(_______)
'''

scissors = '''
    _________
___'    _____)____
        (__________)
        (__________)
        (____)
___.___(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input(f"What do you choose?\nType 0 for Rock\nType 1 for Paper\nType 2 for Scissors\nYour choice: "))
if user_choice >= 3 or user_choice < 0:
    print("Invalid number - LOSER")
else:
    computer_choice = random.randint(0, 2)
    print(f"Computer's choice: {computer_choice}")
    print(game_images[computer_choice])
    print(f"You decided to try: {user_choice}")
    if user_choice == 0 and computer_choice == 2:
        print("YOU WIN")
    elif computer_choice == 0 and user_choice == 2:
        print("YOU LOSE")
    elif computer_choice > user_choice:
        print("YOU LOSE")
    elif computer_choice < user_choice:
        print("YOU WIN")
    elif computer_choice == user_choice:
        print("DRAW")
    else:
        print("Invalid number - LOSER")
