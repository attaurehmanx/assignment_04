adult = 18
def age_adult(age):
    if age >= adult:
        return True
    
    return False


def main():
    age = int(input("How old are you: "))
    print(age_adult(age))

if __name__ == '__main__':
    main()