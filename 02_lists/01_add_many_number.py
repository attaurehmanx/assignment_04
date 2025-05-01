
def add_num(numbers)->int :

    sum_of_all_num: int = 0

    for num in numbers:
        sum_of_all_num += num

    return sum_of_all_num

def main():
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum = add_num(numbers)
    print(sum)

if __name__ == '__main__':
    main()
