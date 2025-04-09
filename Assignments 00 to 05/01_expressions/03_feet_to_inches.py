inches_in_foot = 12

def main():
    feet:float = float(input("Enter your number of feet: "))
    print("Calculating the number of inches in a feet")
    inches:float = feet * inches_in_foot
    print("That is ", inches , "inches!")

if __name__ == '__main__':
    main()