import random
DONE_LIKELIHOOD = 0.2

def chaotic_count():
    for i in range(10):
        curr_count = i + 1
        if done():
            return
        print(curr_count)

def done():
    if random.random() < DONE_LIKELIHOOD:
        return True
    else:
        return False
    
def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_count()
    print("I am done")

if __name__ == '__main__':
    main()