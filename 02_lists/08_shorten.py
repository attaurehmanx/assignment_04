max_length = 5

def shorten(lst):
    while len(lst)  > max_length:
        pop_ele = lst.pop()
        print(pop_ele)



def short():

    lst = []

    ele = input("Enter a element and press enter to stop: ")
    while ele != "":
        lst.append(ele)
        ele = input("Enter a element and press enter to stop: ")
    return lst
    

def main():
    lst = short()  
    shorten(lst) 
    

if __name__ == '__main__':
    main()


