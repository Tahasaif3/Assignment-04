# Project 4: Rock Paper Scissor Game
# Rock Paper Scissor Game

import random

user_wins = 0
computer_wins = 0

# Options for the game choices
options = ["rock", "paper", "scissors"]

print("\n🎮 Welcome to Rock, Paper, Scissors Game! 🎮")
print("Type Rock/Paper/Scissors to play or Q to quit.\n")

while True:
    player = input("Your choice (Rock/Paper/Scissors or Q to quit): ").lower()

    if player == "q":
        print("\nThanks for playing! 🎉")
        print(f"Final Score - You: {user_wins}, Computer: {computer_wins}")
        break

    if player not in options:
        print("⚠️ Invalid choice! Please try again.\n")
        continue

    # Computer randomly selects an option
    computer = random.choice(options)

    print(f"\n📌 You chose: {player}")
    print(f"💻 Computer chose: {computer}\n")

    if player == computer:
        print("🤝 It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("🎉 You win this round!")
        user_wins += 1
    else:
        print("😢 Computer wins this round!")
        computer_wins += 1

    print(f"📊 Score - You: {user_wins}, Computer: {computer_wins}\n")

print("\nMade with ❤️ by Taha Saif")