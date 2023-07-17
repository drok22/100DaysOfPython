import random
from HangmanArt import logo, stages
from HangmanWords import word_list
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# all words available in game
chosen_word = random.choice(word_list)
word_len = len(chosen_word)
display = []
end_of_game = False
lives = 6

#temp
print(f'psst, the solution is {chosen_word}')

for letter in chosen_word:
    display += '-'

print(logo)
print(stages[lives])

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    match_found = False

    if guess in display:
        print(f'you already guessed {guess}')
    elif guess not in chosen_word:
        lives -= 1
        print(f'{guess} is not found in the word. {lives} lives left.')

        if lives == 0:
            end_of_game = True
    else:
        for position in range(word_len):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                match_found = True

    if not '-' in display:
        end_of_game = True

    print(stages[lives])
    print(display)

if lives > 0:
    print('You win!')
else:
    print('You lose... Play again!')