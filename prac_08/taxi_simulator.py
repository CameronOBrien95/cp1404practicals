from prac_08.car import Car
from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi

MENU = "1) choose taxi\n2) Drive\n3) Bill\n4) Quit"
def main():
    taxis = [Taxi("Prius", 100), Taxi("Kia", 150), SilverServiceTaxi("Hummer", 200, 4)
        ,SilverServiceTaxi("Limo", 250, 6)]
    total_bill = 0
    print(MENU)
    choice = int(input("your choice"))
    while choice != 4:
        if choice == 1:
            print("Pick taxi")
        elif choice == 2:
            print("Drive")
        elif choice == 3:
            print("Bill")

main()