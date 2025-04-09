import math

def main():
    ab:float = float(input("Enter the Length of AB: "))
    ac:float = float(input("Enter the Length of AC: "))

    bc: float = (ab**2 +  ac**2) ** 0.5
    print(f"The Hypotenuse (BC) of the right triangle with sides AB = {ab} and AC = {ac} is: {bc:.2f}")

if __name__ == "__main__":
    main()