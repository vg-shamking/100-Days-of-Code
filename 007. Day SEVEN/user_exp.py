import random
import hang_art
from word_list import word_list

print(hang_art.logo[0])
end_of_game = False

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f"Pssst... the solution is {chosen_word}.")

lives = 6

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOU LOSE")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("YOU WIN")

    print(hang_art.stages[lives])
