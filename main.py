import os
import random
from word import words, figure

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    word = random.choice(words).lower()
    word_display = ['_' for _ in word]
    hint_index = random.randint(0, len(word) - 1)
    word_display[hint_index] = word[hint_index]

    lives = len(figure) - 1

    while lives > 0:
        clear_screen()
        print(figure[len(figure) - 1 - lives])
        print("\nWord:", ' '.join(word_display))
        guess = input("Guess a letter: ").lower()

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    word_display[i] = guess
        else:
            lives -= 1

        if "_" not in word_display:
            clear_screen()
            print("You guessed the word:", word)
            print("Congratulations! You won!")
            break

    else:
        clear_screen()
        print(figure[-1])
        print(f"The word was: {word}")
        print('You lost! Better luck next time.')

print("""
 _   _                                         
| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
|  _  | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/                       
""")
print("                              By: Pranav Srikanth")
main()
