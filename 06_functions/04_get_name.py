def get_name():
    user = input("enter your name: ")
    return user

def main():
    name = get_name()
    print(f"Howdy! {name} 🤠")

if __name__ == '__main__':
    main()