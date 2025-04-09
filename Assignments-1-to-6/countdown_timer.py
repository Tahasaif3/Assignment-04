# Project 5: Countdown Timer
# Countdown Timer

import time
import sys

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timeformat = f"{mins:02d}:{secs:02d}"
        sys.stdout.write(f"\r⏳ Time Left: {timeformat} ")
        sys.stdout.flush()
        time.sleep(1)
        seconds -= 1

    print("\n🎉 00:00 ⏳ Time's Up!")

# Get user input for the countdown timer
print("⏳ Countdown Timer")
try:
    t = int(input("Enter time in seconds: "))
    countdown_timer(t)
except ValueError:
    print("⚠️ Please enter a valid number!")

print("\n Made with ❤️ by Taha Saif")
