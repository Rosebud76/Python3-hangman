import random

def hangman():
    words = ['python', 'java', 'ruby', 'javascript', 'html', 'css']
    word = random.choice(words)
    guessed_letters = []
    tries = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while tries > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        if guess not in word:
            tries -= 1
            print("Wrong guess! You have", tries, "tries left.")

            if tries == 0:
                print("You lost! The word was", word)
                return

        guessed_letters.append(guess)

        word_progress = ""
        for letter in word:
            if letter in guessed_letters:
                word_progress += letter + " "
            else:
                word_progress += "_ "

        print(word_progress)

        if "_" not in word_progress:
            print("Congratulations! You guessed the word", word)
            return

    print("Out of tries. Game over!")

hangman()
