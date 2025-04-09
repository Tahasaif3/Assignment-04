# Project 4: A Unique Hangman Game
# Hangman Game

import random

def hangman_game():
    words = ['typescript', 'interface', 'function', 'callback', 'variable', 'enum', 'tuples', 'asynchronous', 'promise', 'compiler']
    word = random.choice(words)
    guessed_letters = set()
    attempts = 7
    word_display = ["_"] * len(word)

    print("\n🎮 Welcome to Hangman! Try to guess the word letter by letter.")
    print(f"The word has {len(word)} letters: {' '.join(word_display)}")

    while attempts > 0:
        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a **single letter**.")
            continue

        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter. Try another!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"✅ Good job! The letter '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    word_display[i] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong guess! You have {attempts} attempts left.")

        print("🔤 Word so far: " + " ".join(word_display))

        if "_" not in word_display:
            print("\n🎉 Congratulations! You guessed the word:", word.upper())
            break

    if "_" in word_display:
        print(f"\n❌ Game Over! The correct word was: {word.upper()}")

    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        hangman_game()
    else:
        print("Thanks for playing! 🎯")

# Start the game
hangman_game()

print("\nMade with ❤️ by Taha Saif");