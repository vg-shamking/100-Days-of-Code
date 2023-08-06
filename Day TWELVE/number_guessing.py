# Welcome to the Number Guessing Game
# I'm thinking of a number between 1 and 100.
# Choose a difficulty. Type 'ease' or 'hard'
# You have 5 attempts remaining to guess the number.
# You have 10 attempts remaining to guess the number.

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """Checks answer against turns. Return the number of turns remaining"""
    if guess > answer:
        print("Too high!")
        return turns - 1
    elif guess < answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'ease' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS
    else:
        print("Incorrect input")


print(logo)


def game():
    print("Welcome to the Number Guessing Game\nI'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")
    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again!")


game()
