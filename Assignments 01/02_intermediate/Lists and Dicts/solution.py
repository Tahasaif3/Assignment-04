# Problem #1: List Practice

def main():
    # Create a list called `fruit_list`
    fruits_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the fruits list
    print(" ".join(fruits_list))


    # Print the length of the list
    print("Length of the list:", len(fruits_list))

    # Add 'mango' at the end of the list
    fruits_list.append('mango')

    # Print the updated list
    print("Updated List:"," ".join(fruits_list))


if __name__ == "__main__":
    main()


# Problem #2: Index Game
def access_element(lst,index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range!"
    
def modify_element(lst,index,new_value):
    try:
      lst[index] = new_value
      return lst
    except IndexError:
        return "Index out of range"
    
def slice_element(lst,start,end):
    try:
      return lst[start:end]
    except IndexError:
        return "Invalid range"

def main():

    my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

    while True:
        print("\nCurrent List:", my_list)
        print("Choose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter your choice (1-4) ")

        if choice == "1":
            index = int(input("Enter the index you want to access: "))
            print("Result: ", access_element(my_list,index))

        elif choice =="2":
           index = int(input("Enter the index you want to modify: "))
           new_value  = input("Enter the new value: ")
           result = modify_element(my_list,index,new_value)
           if type(result) == list:
             print("Updated List:", result)
           else:
             print("Error:", result)
        
        elif choice == "3":
           start = int(input("Enter the start index: "))
           end = int(input("Enter the end index: "))
           print("Sliced List: ", slice_element(my_list,start, end))

        elif choice == "4":
            print("Exiting the game. Goodbye!")
            break

        else:
           print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()