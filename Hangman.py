import random
import time

# Initial Steps to invite in the game:
print("\nWelcome to Hangman game by Popa Alexandru!\n")
name = input("Enter your name: ")
print(f"Hello {name.capitalize()}! The game is about to start! \nBest of Luck!")
time.sleep(1.5)
print()
time.sleep(1.5)
print("You can guess 4 wrong letters, at the 5th, you hang.")
time.sleep(1.5)
print("Let's play Hangman!\n")
time.sleep(1.5)
print("Choosing a word from our vocabulary ", end="")
for _ in range(10):
    time.sleep(0.21)
    print(".", end="")
time.sleep(0.21)
print(" done\n")
time.sleep(0.5)


# The parameters we require to execute the game:
def main():
    global count
    global discovered
    global display
    global original_word
    global word
    global already_guessed
    global wrong_guesses
    global length
    global play_game

    def select_word():
        # words: list of words from file
        with open("words.txt") as words:
            words = words.read().splitlines()
        # returns 1 word at random from a file of 83667 words.
        return random.choice(words).lower()

    word = select_word()
    original_word = word
    length = len(word)
    count = 0
    discovered = ["_"] * length
    display = " ".join(discovered)
    already_guessed = []
    wrong_guesses = []
    play_game = ""

# A loop to re-execute the game when the first round ends:
def play_loop():
    global play_game
    play_game = input("Do you want to play a new game? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thank you for playing! Don't be a stranger, now! ;)")
        exit()

# Initializing all the conditions required for the game:
def hangman():
    global count
    global discovered
    global display
    global word
    global already_guessed
    global wrong_guesses
    global play_game
    max_guesses = 5
    guess = input("This is the Hangman Word: " + display + " Guess a letter: \n")
    guess = guess.strip().lower()
    if len(guess) == 0 or len(guess) >= 2 or guess.isdigit():
        print("Invalid Input, Try a letter\n")
        hangman()

    elif guess in word:
        def find(char, word):
            return [i for i, letter in enumerate(word) if letter == char]
        already_guessed.extend([guess])
        index = find(guess, word)
        word = word.replace(guess,"_")
        for i in index:
            discovered[i] = guess
        display = " ".join(discovered)
        print(display + "\n")

    elif guess in already_guessed or guess in wrong_guesses:
        print(f"You have already tried '{guess}'. Please try another letter.\n")

    else:
        count += 1
        wrong_guesses.extend([guess])

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(max_guesses - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(max_guesses - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     |\n"
                 "  |     |\n"
                 "  |     O\n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(max_guesses - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |    /|\ \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(max_guesses - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "  |        \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:"," ".join(list(original_word)))
            play_loop()

    if word == '_' * length:
        print("Congratulations! You have guessed the word correctly!")
        play_loop()

    elif count != max_guesses:
        hangman()


main()
hangman()