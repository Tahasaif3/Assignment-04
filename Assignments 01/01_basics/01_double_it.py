def double_it():
    number = "Enter the number: "
    curr_Value = int(input(number))

    while curr_Value < 100:
        curr_Value = curr_Value * 2
        print(curr_Value, end=" ")

double_it()