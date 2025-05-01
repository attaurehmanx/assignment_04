def data():
    name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    return name, l_name, email

def main():
    print(f"Your data is here {data()}")

if __name__ == '__main__':
    main()