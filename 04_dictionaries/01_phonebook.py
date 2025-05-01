

def read_num():

    dic = {}
    name = input("Enter your name :")

    while True:
        number = input("Enter your num or press enter for next step :")

        if number == "":
            break

        num = int(number)

        dic[name] = num
    return dic

def print_phonebook(dic):
    for phone in dic:
        print(f"{phone} {dic[phone]}")

def lookup_phonebook(dic):

    while True:
        search_name = input("Enter your name for searching a phone number or press enter for exit :")
        if search_name == "":
            break

        if search_name in dic:
            print(f"Your Phone number is {dic[search_name]}")
        else:
            print("Not found")

def main():
    read = read_num()
    print_phonebook(read)
    lookup_phonebook(read)

if __name__ == '__main__':
    main()