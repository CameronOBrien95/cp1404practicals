from prac_08.taxi import Taxi



def main():
    """Demo test code to show how to use car class."""
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print("{}\n${}".format(taxi, taxi.get_fare()))
    taxi.start_fare()
    taxi.drive(100)
    print("${}".format(taxi.get_fare()))





main()