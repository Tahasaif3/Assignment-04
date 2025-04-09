def main():
    fruits = {
        "apple": 10.0,
        "durian": 25.0,
        "jackfruit": 12.5,
        "kiwi": 8.0,
        "rambutan": 7.0,
        "mango": 9.0
 }

    total = 0
    for fruit,price in fruits.items():
        quantity_str = input(f"How many ({fruit}) do you want?: ")
        quantity = int(quantity_str) if quantity_str else 0
        total += quantity * price

    print(f"Your Total Bill is {total} $")

if __name__ == "__main__":
    main()