MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_element = lst.pop()
        print(last_element)


def main():
    number_of_elements = int(input("Enter the number of elements in the list: "))
    user_list = []

    for _ in range(number_of_elements):
        element = input("Enter an element: ")
        user_list.append(element)
    
    print("Original List: ", user_list)
    shorten("Romeved Element: ", user_list)
    print("Final list:", user_list)

if __name__ == "__main__":
    main()