
def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    print(count)


def user_num_lst():

    lst= []
    user = input("Enter an integer or press enter to stop.")

    while user != "":
        if user == "":
            break
        user_int = int(user)
        lst.append(user_int)
        user = input("Enter an integer or press enter to stop.")
    return lst


def main():
    x = user_num_lst()
    count_even(x)

if __name__ == '__main__':
    main()
