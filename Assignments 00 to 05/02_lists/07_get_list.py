def main():
    lst = []
    while True:
          value = input("Enter a value or press enter to quit: ")
          if value == "":
               break
          lst.append(value)
    print("Here is the List: \n", lst)

   
if __name__ == '__main__':
    main()