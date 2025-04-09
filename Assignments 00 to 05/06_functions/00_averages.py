def find_average(num1, num2):
    average = (num1 + num2) / 2
    return average

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    average = find_average(num1, num2)
    print(f"The average of {num1} and {num2} is {average:.2f}")

if __name__ == "__main__":
    main()
