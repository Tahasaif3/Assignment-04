def main():
    phoneBook = {}

    while True:
        name = input("Enter a name (or press Enter to stop): ")
        if name == "":
            break
        number = input("Enter the phone number: ")
        phoneBook[name] = number

    print("\nPhonebook entries:")
    for name,number in phoneBook.items():
        print(f"{name} -> {number}")

    print("\nPhone number lookup:")
    while True:
        search = input("Enter a name to lookup (or press Enter to quit): ")
        if search == "":
            break
        if search in phoneBook:
            print(f"{search}'s number is: {phoneBook[search]}")
        else:
            print(f"{search} is not in the phonebook.")

if __name__ == "__main__":
    main()

    