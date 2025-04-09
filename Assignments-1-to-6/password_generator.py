# Project 7: A Secure Password Generator 
# Password Generator

import random
import string
import sys
import time

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Generating Password Loading Animation
def loading_animation(text="Generating Password"):
    print(text, end="", flush=True)
    for _ in range(5):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("\n")

# User Input for Generating The Pasoword
print("🔐 Welcome to Secure Password Generator!")
try:
    length = int(input("Enter the desired password length (min 6): "))
    if length < 6:
        print("⚠️ Password length should be at least 6 characters!")
    else:
        loading_animation()
        password = generate_password(length)
        print("✅ Your Secured Generated Password: ", password)
except ValueError:
    print("⚠️ Please enter a valid number!")

print("Made with ❤️ by Taha Saif")
