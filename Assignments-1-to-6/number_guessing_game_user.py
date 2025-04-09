# Project 3: Number Guessing Game (User)
# Number Guessing Game (User)

import random

def guess_the_number():
    print("\n🎯 Project 3: Guess The Number Game (User) 🎯")
    print("Try to guess the number between 1 and 100!")

    random_number = random.randint(1, 100)
    attempts = 3

    while attempts > 0:
        try:
            guess = int(input(f"\nYou have {attempts} attempts left. Enter your guess: "))

            if guess < 1 or guess > 100:
                print("⚠️ Please enter a number between 1 and 100!")
                continue

            if guess < random_number:
                print("🔼 Too low! Try again.")
            elif guess > random_number:
                print("🔽 Too high! Try again.")
            else:
                print("🎉 Congratulations! You guessed the correct number! 🎉")
                break

            attempts -= 1

            if attempts == 0:
                print(f"❌ Game Over! The correct number was {random_number}. Better luck next time! 🎲")
        except ValueError:
            print("⚠️ Invalid input! Please enter a valid number.")

    # Asking the user if they want to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        guess_the_number()
    else:
        print("Thanks for playing! 🎮")

# Start the game
guess_the_number()

print("\nMade with by ❤️ Taha Saif\n")