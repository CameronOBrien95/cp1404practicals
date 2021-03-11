number_of_items = int(input("How many items are there? "))
while number_of_items <= 0:
    print("Invalid number of items\n")
    number_of_items = int(input("How many items are there? "))
total_price = 0
for i in range(0, number_of_items):
    prices = int(input("Price of item $"))
    while prices <= 0:
        print("Invalid price\n")
        prices = int(input("Price of item $"))
    total_price += prices
if total_price > 100:
    total_price = total_price - total_price * .10
print("Total price for {} items is ${}".format(number_of_items, total_price))
