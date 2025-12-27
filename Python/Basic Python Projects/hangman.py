import random
words = ("apple", "orange", "banana", "coconut", "pineapple")
'''# using random module we will pick one of the above words at random.
#we can guess the word one letter at a time. once, we reach 6 incorrect guesses we will loose the game.
before each guess we will display some ascii art , which we will call as the hangman_art.
This hangman_art will be a dictionary in which each key value pair 
contains a tuple.'''

#dict of key, key will represent incorrect no. of guesses.
hangman_art = {
    0: (

    ),
    1: (
        "  +---+",
        "  |   |",
        "  O   |",
        "      |",
        "      |",
        "      |",
        "========="
    ),
    2: (
        "  +---+",
        "  |   |",
        "  O   |",
        "  |   |",
        "      |",
        "      |",
        "========="
    ),
    3: (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|   |",
        "      |",
        "      |",
        "========="
    ),
    4: (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        "      |",
        "      |",
        "========="
    ),
    5: (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        " /    |",
        "      |",
        "========="
    ),
    6: (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        " / \\  |",
        "      |",
        "========="
    )
}

'''for line in hangman_art[6]:
    print(line)'''

#we will declear various fucntions we will need throughout this programme.

# define funtion to display our hangman.
#to display our man we need to know the number of incorrect guesses.
def display_man(wrong_guesses):
   for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))
#hint is going to be a list of unserscore scharaters. for each character we guess right
#we will flip the udnerscore.

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer=random.choice(words)
    hint=["_"]*len(answer)
    wrong_guesses=0
    guessed_letters= set()
    is_running=True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input('enter a letter:').lower()

        if len(guess)!= 1 or not guess.isalpha():
            print('invalid input')
            continue

        if guess in guessed_letters:
            print(f'this {guess} is already marked')
            continue
        guessed_letters.add(guess)
        if guess in answer:
            for index in range(len(answer)):
                if answer[index]== guess:
                    hint[index] = guess
        else:
            wrong_guesses+=1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("u won")
            is_running=False
        elif wrong_guesses>= len(hangman_art)-1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("u lose")
            is_running=False





if __name__ == "__main__":
    main()











