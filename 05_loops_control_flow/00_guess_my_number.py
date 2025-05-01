import random

def main():
    secret_num = random.randint(1, 99)

    print("Guess my number!")

    guess = int(input("enter your guess number :"))

    while guess != secret_num:
        if guess > secret_num:
            print("guess is to high")
        else:
            print("guess is to low")
        
            
        
        guess = int(input("enter your guess number :"))
    print(f"your guess is right you win! the guess was {secret_num}")

if __name__ == '__main__':
    main()