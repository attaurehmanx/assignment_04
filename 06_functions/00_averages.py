def ava(a, b):
    c = a + b / 2
    return c

def main():
    ava_1 = ava(2, 4)
    ava_2 = ava(4, 5)
    final = ava(ava_1, ava_2)
    
    print(f"average_1: {ava_1}")
    print(f"average_2: {ava_2}")
    print(f"final average answer is {final}")

if __name__ == '__main__':
    main()

    