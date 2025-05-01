def first_ele(lst):
    
    print(lst[0])

def one_ele():
    lst = []

    ele_list = input("enter an item or press to exit: ")
    while ele_list != "":
        lst.append(ele_list)
        ele_list = input("enter an item or press to exit: ")
    print(lst)
    return lst
    

def main():
    x = one_ele()
    first_ele(x)
    

if __name__ == '__main__':
    main()
