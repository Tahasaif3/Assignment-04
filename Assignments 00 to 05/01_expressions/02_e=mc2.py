def main():
    C = 29979245855
    mass_in_kg = float(input("Enter your mass in kg: "))
    energy_in_Joules:float = mass_in_kg * (C**2)
    print("Energy in Joules = m * C**2")
    print("m = " + str(mass_in_kg) + " kg")
    print("c = " + str(C) + "m/s")
    print(str(energy_in_Joules) +  " joules of energy!")

if __name__ == '__main__':
    main()