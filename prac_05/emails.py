"""
CP1404/CP5632 Practical
Email to name dictionary
"""

email_name = {}
email = input("Email: ")
valid = False
while email != "":
    name = email.split("@")[0]
    name = name.replace(".", " ").title()
    choice = input("Is your name {}? (Y/n)".format(name)).upper()
    if choice != 'Y':
        name = input("What is your name ?")
    email_name[email] = name
    email = input("Email: ")

for email in email_name:
    print("{} ({})".format(email_name[email], email))