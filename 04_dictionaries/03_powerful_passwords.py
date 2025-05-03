from hashlib import sha256
def login(email, login_stored, password_tocheck):

    if login_stored[email] == hash_pass(password_tocheck):
        return True
    return False


def hash_pass(password):

    return sha256(password.encode()).hexdigest()

def main():
    login_stored = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
        "student@stanford.edu": "68bf0109c6f8a87bfa96d1ecd9503326ba35cf4a6086988a1d2c8a20fbef00d1"
    }

    print(login("example@gmail.com", login_stored, "strong"))
    print(login("example@gmail.com", login_stored, "password"))

    print(login("code_in_placer@cip.org", login_stored, "hello"))
    print(login("code_in_placer@cip.org", login_stored, "hi"))

    print(login("student@stanford.edu", login_stored, "education"))
    print(login("student@stanford.edu", login_stored, "knowledge"))
    


if __name__ == '__main__':
    main()