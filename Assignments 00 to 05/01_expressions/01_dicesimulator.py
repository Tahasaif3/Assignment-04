import random 

NUM_SIDES = 6

def ROLL_DICE():
    dice1:int=random.randint(1,NUM_SIDES)
    dice2:int=random.randint(1,NUM_SIDES)
    total:int=dice1 + dice2
    print("Total of two dice:", total)



def main():
    dicee1:int = 10
    print("dice1 starts as " + str(dicee1) )
    ROLL_DICE()
    ROLL_DICE()
    ROLL_DICE()
    print("Dice1 is " + str(dicee1))



if __name__ == '__main__':
    main()