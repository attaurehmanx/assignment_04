
max_num = 10000

def main():
    
    a = 0
    b = 1
    while a <= max_num:
        print(a)
        two_num = a + b
        a = b
        b = two_num

if __name__ == '__main__':
    main()