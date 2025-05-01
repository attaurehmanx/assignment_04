
AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print(f"Please type the following affirmation: {AFFIRMATION}")

    user = input()
    while user != AFFIRMATION:
        print(f"Thats not a affirmation.")

        print("please write a right affirmation.")
        user = input()
    print("Thats right affirmation.")

if __name__ == '__main__':
    main()