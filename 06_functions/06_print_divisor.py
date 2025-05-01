def divible_num(num):
    print("Here are the divisor of ",num)
    for i in range(num):
        curr_num = i + 1
        if num % curr_num == 0:
            print(curr_num)

def main():
    num = int(input("Enter an integer: "))
    divible_num(num)

if __name__ == '__main__':
    main()