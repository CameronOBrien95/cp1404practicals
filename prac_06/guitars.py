from prac_06.guitar import Guitar


def main():
    guitars = []
    name = input("Guitar name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print("{} ({}) : {} added.".format(name, year, cost))
        name = input("Guitar name: ")

    for i, guitar in enumerate(guitars):
        vintage_string = " "
        if guitar.is_vintage():
            vintage_string = "(Vintage)"
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                  vintage_string))


main()
