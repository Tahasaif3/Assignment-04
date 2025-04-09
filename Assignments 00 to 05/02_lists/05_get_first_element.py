def get_first_element(lst):
    print("The First Element is: " , lst[0])


def main():
    number_of_elements = int(input("Enter the number of elements in the list: "))
    user_list = []

    for _ in range(number_of_elements):
        element = input("Enter an element: ")
        user_list.append(element)

    get_first_element(user_list)
    
if __name__ == "__main__":
    main()

    