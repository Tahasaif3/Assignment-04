def double_numbers(numbers:list):
    doubled_list = []
    for num in numbers:
        doubled_list.append(num*2)
    return doubled_list

numbers = [2,4,6,8,10]
doubled_numbers = double_numbers(numbers)
print("Doubled list:", doubled_numbers)
