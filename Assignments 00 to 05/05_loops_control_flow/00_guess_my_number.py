import random

def main():
    secret_number = random.randint(1,100)
    print("I am thinking of a number between 1 and 99...")

    while True:
        guess = int(input("Take a guess: "))
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:   
            print("Congrats! The number was: ", secret_number)
            break

if __name__ == "__main__":
    main()
2