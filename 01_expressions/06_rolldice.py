# Simulate rolling two dice, and prints results of each roll as well as the total.

import random

dice_points = 6

def main():
    die1 = random.randint(1, dice_points)
    die2 = random.randint(1, dice_points)
    total = die1 + die2

    print(f'die1 is {die1} , die2 is {die2} and total is {total}')

if __name__ == '__main__':
    main()