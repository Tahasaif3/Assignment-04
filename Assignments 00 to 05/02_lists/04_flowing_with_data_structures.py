def add_three_coppies(lst,data):
    lst.append(data)
    lst.append(data)
    lst.append(data)


def main():
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before: ", my_list)
    add_three_coppies(my_list, message)
    print("List After: ",my_list)

if __name__ == "__main__":
    main()
