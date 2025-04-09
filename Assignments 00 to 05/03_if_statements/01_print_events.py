count = 20
num = 0

def main():
    global num
    for _ in range(count):
        print(num) # To print in Vertical
        print(num,end=" ") # To print in one line
        num+=2

if __name__ == "__main__":
    main()

