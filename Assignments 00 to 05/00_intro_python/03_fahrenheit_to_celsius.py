# Fahrenheit to Celsius Converter

def main():
    fahrenheit_temperature = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit_temperature - 32) * 5.0 / 9.0

    print(f"Temperature: {fahrenheit_temperature}F = {celsius}C")

if __name__ == '__main__':
    main()

