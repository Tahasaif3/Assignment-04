# Project 2: Number Guessing Game (Computer)
# Number Guessing Game (Computer)

import random

def guess_the_number():
    print("\n🎯 Project 2: Guess The Number Game By Computer! 🎯")
    random_number = random.randint(1, 100)
    guesses_left = 3

    # Welcome Message on the Console
    print("Welcome To The Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {guesses_left} attempts to guess the correct number.\n")

    while guesses_left > 0:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("⚠️ Please enter a number between 1 and 100.")
                continue

            if guess == random_number:
                print("🎉 Congratulations! You guessed the correct number! 🎉")
                break
            elif guess < random_number:
                print("🔼 Too low! Try again.")
            else:
                print("🔽 Too high! Try again.")

            guesses_left -= 1
            if guesses_left > 0:
                print(f"You have {guesses_left} guesses left.\n")
            else:
                print(f"❌ Game Over! The correct number was {random_number}. Better luck next time! 🎲")

        except ValueError:
            print("⚠️ Invalid input! Please enter a valid number.\n")

# start the game
guess_the_number()

print("\nMade with by ❤️ Taha Saif\n")
