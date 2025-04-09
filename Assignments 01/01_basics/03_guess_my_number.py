import random

def main():
 secret_number = int(random.randint(1, 99))

 print("I am Thinking of a number between 1 and 100!")

 guess = int(input("Guess a number: "))

 while guess != secret_number:
  if guess < secret_number:
   print("your guess is two low!")
  else: 
   print("your guess is too high!")

  print()
  guess = int(input("Enter a new guess: "))

 print(f"Congrats! you guessed it The number was {secret_number} ") 

if __name__ == '__main__':
    main()


