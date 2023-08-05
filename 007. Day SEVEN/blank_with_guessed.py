import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(f"Pssst... the solution is {chosen_word}.")
guess = input("Guess a letter: ").lower()

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(dis)
