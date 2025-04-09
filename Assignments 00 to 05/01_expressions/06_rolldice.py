import random

sides = 6

def main():

    die1 = random.randint(1,sides)
    die2 = random.randint(1,sides)
    total = die1 + die2

    print(f"Dice have {sides} sides each") 
    print("First Rolled Die: " , die1)
    print("Second Rolled Die: " , die2)
    print("Total of two dice: " , total)

if __name__ == "__main__":
    main()

