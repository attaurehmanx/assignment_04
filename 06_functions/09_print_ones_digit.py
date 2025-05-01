def one_dig(num):
    print(f"The one digit is {num % 10}")

def main():
    num = int(input("Enter a number: "))
    one_dig(num)

if __name__ == '__main__':
    main()

