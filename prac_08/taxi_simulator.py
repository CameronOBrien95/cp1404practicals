from prac_08.car import Car
from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), Taxi("Kia", 150), SilverServiceTaxi("Hummer", 200, 4)
        , SilverServiceTaxi("Limo", 250, 6)]
    total_bill = 0
    choice = input("{}\n>>>".format(MENU)).lower()
    current_taxi = None
    while choice != "q":
        if choice == "c":
            display_taxis(taxis)
            taxi_choice = int(input("Please choose a taxi"))
            current_taxi = taxis[taxi_choice]
            print("{} Chosen".format(taxis[taxi_choice]))
        elif choice == "d":
            if current_taxi is None:
                print("You need to pick a taxi first")
            else:
                current_taxi.start_fare()
                distance = int(input("How far would you like to drive? "))
                current_taxi.drive(distance)
                fare_cost = current_taxi.get_fare()
                total_bill += fare_cost
                print("your trip cost you ${:.2f}".format(fare_cost))
        print("Your total bill is ${:.2f}".format(total_bill))
        choice = input("{}\n>>>".format(MENU)).lower()


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i + 1, taxi))


main()
