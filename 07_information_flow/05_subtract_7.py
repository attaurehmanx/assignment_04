def main():
    num = 7
    sub = subtract_seven(num)
    print("This should be zero", sub)


def subtract_seven(num):
    num = num - 7
    return num

if __name__ == '__main__':
    main()