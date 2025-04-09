def main():
    dividend = int(input("Enter the number to be divided: "))
    diviser = int(input("Enter the number to be  Divided By:"))
    quotient:int = dividend // diviser
    remainder:int = dividend % diviser
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))

if __name__ == "__main__":
    main()
