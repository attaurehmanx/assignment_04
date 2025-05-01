
def multi_msg(message, repeat):
    for i in range(repeat):
        print(message)

def main():
    user_msg = input("Enter a message :")
    user_repeat = int(input("Enter a value to repeat the msg: "))
    multi_msg(user_msg, user_repeat)

if __name__ == '__main__':
    main()
    