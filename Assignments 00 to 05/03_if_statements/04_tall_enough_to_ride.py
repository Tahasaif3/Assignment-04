def tall_enough_extension():
    while True:
        height = input("How tall are you? (Press Enter to quit): ")
        
        if height == "":
            break  # Exit the loop if nothing was entered
        
        height = int(height)
        if height >= 50:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

if __name__ == "__main__":
    tall_enough_extension()
