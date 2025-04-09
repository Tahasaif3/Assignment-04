def num_in_stock(fruit):
    inventory = {
        "apple": 50,
        "banana": 30,
        "pear": 1000,
        "grape": 200,
        "orange": 0
    }
    
    return inventory.get(fruit, 0)

def main():
    fruit = input("Enter a fruit: ")
    stock = num_in_stock(fruit)
    
    if stock > 0:
        print("This fruit is in stock! Here is how many:", stock)
    else:
        print("This fruit is not in stock.")

if __name__ == "__main__":
    main()
