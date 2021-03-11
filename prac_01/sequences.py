print("\nMenu\n(1) Show even numbers from (x) to (y).\n(2) Show odd numbers from (x) to (y).\n(3) show the squares from"
      " (x) to (y)\n(4) Quit.")
choice = int(input("what is your choice ?\n"))
while choice != 4:
    if choice != 1 and choice != 2 and choice != 3 and choice != 4:
        print("invalid choice")
    else:
        first_number = int(input("pick your first number"))
        second_number = int(input("pick your second number"))

    if choice == 1:
        is_even = first_number % 2
        if is_even == 0:
            for i in range(first_number, second_number, 2):
                print(i)
        else:
            for i in range(first_number + 1, second_number, 2):
                print(i)

    elif choice == 2:
        is_odd = first_number % 2
        if is_odd == 1:
            for i in range(first_number, second_number, 2):
                print(i)
        else:
            for i in range(first_number - 1, second_number, 2):
                print(i)

    elif choice == 3:
        for i in range(first_number, second_number):
            print(i ** 2)
    else:
        print("Goodbye")
    print("\nMenu\n(1) Show even numbers from (x) to (y).\n(2) Show odd numbers from (x) to (y).\n(3) show the squares "
          "from (x) to (y).\n(4) Quit.")
    choice = int(input("what is your choice ?\n"))
print("goodbye")
