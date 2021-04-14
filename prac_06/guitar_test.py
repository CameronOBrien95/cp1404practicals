from prac_06.guitar import Guitar

name = "Gibson L-5 CES"
year = 1950
cost = 99999

guitar = Guitar(name, year, cost)
print("{} get_age() - expected 71. got {}".format(name, guitar.get_age()))
print("Name: {}\nYear: {}\nCost: {}".format(guitar.name, guitar.year, guitar.cost))
print("{} is_vintage() - expected True. got {}".format(name, guitar.is_vintage()))
