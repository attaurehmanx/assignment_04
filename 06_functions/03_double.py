def double_num(num):
    return num * 2

def main():
    num =int(input("Enter a number to make it double: "))
    dou = double_num(num)
    print(f"Double is {dou}")

if __name__ == '__main__':
    main()