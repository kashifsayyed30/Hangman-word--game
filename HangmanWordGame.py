import random
import hangman_art
import hangman_words
from replit import clear
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_of_game = False
lives = 6
#word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)

print(hangman_art.logo)


length = len(chosen_word)
#print(f"Length of the chosen word is: {length}")
display_list = [] # empty list
for letter in chosen_word:
    display_list += '_'
print("================================================")
#print(display_list)
blank = '_'

while not end_of_game:
    guess = input("Guess a letter:  ").lower()
    clear()
    if guess in display_list:
        print(f"You have already guessed {guess}")
    for position in range(length):
        letter = chosen_word[position]
        if letter == guess:
            display_list[position] = guess
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Loose")
    #print(f"The word was: {chosen_word}")
    print(f"{' '.join(display_list)}")
    if blank not in display_list:
        end_of_game = True
        print("You Won!!")
        
    print(hangman_art.stages[lives])
    #print(f"The word was: {chosen_word}")
        
