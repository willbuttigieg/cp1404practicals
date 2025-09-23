def main():
    password = get_valid_password()
    print_password(password)


def print_password(password: str):
    print("*" * len(password))


def get_valid_password() -> str:
    password = str(input("Enter the password: "))
    while len(password) < 8:
        print("Password must be at least 8 characters long")
        password = str(input("Enter the password: "))
    return password


main()
