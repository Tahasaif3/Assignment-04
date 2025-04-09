def main():
    year = int(input("Please enter a year: "))
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("That's a Leap year")
    else:
        print("That's not a Leap year")

if __name__ == "__main__":
    main()
