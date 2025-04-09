def get_last_element(lst):
    print("The Last Element is: " , lst[-1])


def main():
    number_of_elements = int(input("Enter the number of elements in the list: "))
    user_list = []

    for _ in range(number_of_elements):
        element = input("Enter an element: ")
        user_list.append(element)

    get_last_element(user_list)
    
if __name__ == "__main__":
    main()

    