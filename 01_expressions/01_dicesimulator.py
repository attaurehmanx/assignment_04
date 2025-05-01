import random

dice_num = 6

def roll_dice():
    roll1 = random.randint(1, dice_num)
    roll2 = random.randint(1, dice_num)

    total = roll1 + roll2
    print(f"dice1 is {roll1} , dice2 is {roll2} and total is {total}")

def main():
    roll1 = 10

    print(f"roll1 is {roll1}")

    roll_dice()
    roll_dice()
    roll_dice()

    print(f"roll1 is {roll1}")

if __name__ == '__main__':
    main()