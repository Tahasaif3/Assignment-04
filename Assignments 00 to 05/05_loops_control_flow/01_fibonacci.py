def main():
    MAX_VALUE = 10000
    a, b = 0, 1

    while a < MAX_VALUE:
        print(a, end=' ')
        a, b = b, a + b
        print()

if __name__ == '__main__':
    main()