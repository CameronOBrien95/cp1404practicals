def main():
    password = get_password()
    while not password:
        print("Invalid password")
        password = get_password()
    print(asterisks_length(password))


def get_password():
    password = input("Please enter a password")
    if len(password) > 12 or len(password) < 6:
        return False
    else:
        return password


def asterisks_length(password):
    asterisk = "*" * len(password)
    return asterisk


main()
