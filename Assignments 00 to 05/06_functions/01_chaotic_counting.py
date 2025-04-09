import random

DONE_LIKEHOOD = 0.3

def done():
    return random.random() < DONE_LIKEHOOD


def count_to_ten():
    for i in range(1,11):
        if done():
            return
        print(i)


def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    count_to_ten()
    print("I am Done!.")

if __name__ == "__main__":  
    main()