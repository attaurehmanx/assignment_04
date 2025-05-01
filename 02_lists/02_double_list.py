def main():
    num = [1,2,3,4,5,6]

    for i in range(len(num)):
        double = num[i]
        num[i] = double * 2
        
    print(num)

if __name__ == '__main__':
    main()