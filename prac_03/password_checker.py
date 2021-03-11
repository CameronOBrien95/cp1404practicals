def main():
    password = get_password()
    while password == "invalid_password":
        password = get_password()
    print(asterisks_length(password))


def get_password():
    password = input("Please enter a password")
    if len(password) > 12 or len(password) < 6:
        return "invalid_password"
    else:
        return password


def asterisks_length(password):
    asterisk = "*" * len(password)
    return asterisk


main()
