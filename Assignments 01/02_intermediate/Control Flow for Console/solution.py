import random

total_rounds = 5
print("🎮 Welcome to High-Low Game!")
print('-' * 100)
score = 0

for round_num in range(1,total_rounds + 1):
  print(f"\n🔵 Round {round_num} of {total_rounds}")
  my_random_number: int = random.randint(1, 100)
  computer_random_number: int = random.randint(1, 100)

  print(f'My random number is {my_random_number}')

  user_guess = input("Do you think my random number is higher or lower than computer's random number? (Type 'higher' or 'lower'): ").strip().lower()

  if (
    (user_guess == "higher" and my_random_number > computer_random_number)
    or
    (user_guess == "lower" and my_random_number < computer_random_number)
  ):
    print("✅ Congratulations! Your guess is correct.")
    print("You got +1 point")
    score += 1
  else:
    print("❌ Sorry, your guess is incorrect.")
    if score > 0:
     score -=1
  print(f"🖥️ Computer's random number was: {computer_random_number}")
  print(f"🎯 Your current score: {score}")

print("\n" + "=" * 50)
print(f"🏆 Your final score: {score} / {total_rounds}")
if score == total_rounds:
    print("🎖️ Outstanding! You guessed everything correctly. You're a High-Low Master! 🏅")
elif score >= total_rounds * 0.7:
    print("👏 Great job! You have a sharp intuition. Keep it up! 🚀")
elif score >= total_rounds * 0.4:
    print("🙂 Not bad! You're getting there. A little more practice and you'll be a pro! 💪")
else:
    print("😅 Better luck next time! Keep playing to improve your guessing skills. 🎲")
print("=" * 50)